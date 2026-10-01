#!/usr/bin/env python3
"""Validate every skill in skills/. Exit 1 on any error.

Per skill:
  - frontmatter: name equals the folder name and follows the Agent Skills
    naming rules; description present and at most 1024 characters
  - size: at most 500 lines; warn above ~5,000 tokens, fail above ~6,000
    (tokens are estimated as bytes / 4)
  - catalogue entries use only the allowed line labels, have a Do,
    Requirement or Use when line, and carry no citations in their header
  - references/evidence.md has exactly one block per catalogue entry, with the
    same grade, and each block has a Finding, Sources or Basis line
  - every source cited in evidence.md can be found in references/sources.md
  - dist/ is up to date
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # noqa: E402

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
GRADES = ("Strong", "Moderate", "Contested", "Framework")
LABELS = ("Do", "Check", "Note", "Caution", "Ethics", "Rules", "Requirement",
          "Formula", "Use when", "Avoid when", "See also", "Verify")
YEAR = r"(?:1[89]|20)\d\d"
# evidence sections that have no counterpart in the catalogue
EXTRA_SECTIONS = {"ux-accessibility": ["Background"], "ux-ethics": ["Three tests"]}
WARN_TOKENS, MAX_TOKENS, MAX_LINES = 5000, 6000, 500


def catalogue(body):
    m = re.search(r"^## The catalogue\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1) if m else ""


def entries(body):
    """Return [(name, header_rest, [bullet lines])] for the catalogue."""
    out, cur = [], None
    for ln in catalogue(body).split("\n"):
        h = re.match(r"^\*\*(.+?)\*\*(?: · (.*))?$", ln)
        if h:
            cur = (h.group(1), h.group(2) or "", [])
            out.append(cur)
        elif cur and ln.startswith("- "):
            cur[2].append(ln)
    return out


def header_grade(rest):
    for part in rest.split(" · "):
        if part.strip().startswith(GRADES):
            return part.strip()
    return ""


def cite_names(cite):
    names = re.findall(r"[A-Z][\w.'\-]*", cite, re.U)
    return [n.rstrip(".") for n in names if n.rstrip(".") not in ("Art",)]


def cite_found(cite, sources_lines):
    cite = cite.strip().strip(".")
    if not cite:
        return True
    year = re.search(YEAR, cite)
    if not year:
        return any(cite.lower() in line.lower() for line in sources_lines)
    names = cite_names(cite[:year.start()])
    for line in sources_lines:
        if year.group(0) not in line:
            continue
        if all(re.search(r"(?<![\w'\-])" + re.escape(n) + r"(?![\w'\-])", line, re.U) for n in names):
            return True
    return False


def inline_cites(text):
    """Author-year citations written inside running text, e.g. (WebAIM 2026)."""
    pat = r"((?:[A-Z][\w.'\-]*(?:, | & | et al\. | )?)+?)(" + YEAR + r")"
    found = []
    for paren in re.findall(r"\(([^()]*)\)", text):
        for piece in re.split(r"[;,] (?=[A-Z])", paren):
            m = re.search(pat, piece, re.U)
            if m and not re.search(r"[a-z] $", piece[:m.start()] + " "):
                found.append((m.group(1) + m.group(2)).strip())
    return found


def check_skill(name):
    errors, warnings = [], []
    base = os.path.join(build.SKILLS_DIR, name)
    text = build.read(os.path.join(base, "SKILL.md"))
    try:
        front, body = build.split_frontmatter(text)
    except ValueError as exc:
        return ["%s: %s" % (name, exc)], []

    fm_name = re.search(r"^name: *\"?([^\"\n]+)\"?$", front, re.M)
    fm_desc = re.search(r"^description: *(.+)$", front, re.M)
    if not fm_name or fm_name.group(1).strip() != name:
        errors.append("frontmatter name must equal the folder name")
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append("name must be lowercase letters, digits and single hyphens, at most 64 characters")
    if not fm_desc:
        errors.append("missing description")
    elif len(fm_desc.group(1).strip().strip('"')) > 1024:
        errors.append("description is over 1024 characters")

    n_lines = text.count("\n") + 1
    n_tokens = len(text.encode("utf-8")) // 4
    if n_lines > MAX_LINES:
        errors.append("SKILL.md has %d lines (limit %d)" % (n_lines, MAX_LINES))
    if n_tokens > MAX_TOKENS:
        errors.append("SKILL.md is about %d tokens (limit %d)" % (n_tokens, MAX_TOKENS))
    elif n_tokens > WARN_TOKENS:
        warnings.append("SKILL.md is about %d tokens (recommended under %d)" % (n_tokens, WARN_TOKENS))

    ev_path = os.path.join(base, "references", "evidence.md")
    src_path = os.path.join(base, "references", "sources.md")
    missing = [p for p in (ev_path, src_path) if not os.path.isfile(p)]
    for p in missing:
        errors.append("missing " + os.path.relpath(p, base))

    # catalogue entries
    ents = entries(body)
    if not ents:
        errors.append("no entries found under '## The catalogue'")
    seen = set()
    for ename, rest, lines in ents:
        if ename in seen:
            errors.append("duplicate entry name '%s'" % ename)
        seen.add(ename)
        if re.search(YEAR, rest):
            errors.append("entry '%s': citations belong in references/evidence.md, not the header" % ename)
        labels = []
        for ln in lines:
            m = re.match(r"^- ([A-Za-z ]+?):", ln)
            if not m or m.group(1) not in LABELS:
                errors.append("entry '%s': line must start with one of %s (got '%s')"
                              % (ename, ", ".join(LABELS), ln[:30]))
            else:
                labels.append(m.group(1))
        if not {"Do", "Requirement", "Use when"} & set(labels):
            errors.append("entry '%s' has no Do, Requirement or Use when line" % ename)

    if missing:
        return ["%s: %s" % (name, e) for e in errors], ["%s: %s" % (name, w) for w in warnings]

    # evidence blocks
    evidence = build.read(ev_path)
    sources_lines = build.read(src_path).split("\n")
    blocks, section = {}, None
    extra_seen = set()
    for chunk in re.split(r"\n(?=##+ )", evidence):
        if chunk.startswith("## "):
            section = chunk.split("\n", 1)[0][3:]
            if section in EXTRA_SECTIONS.get(name, []) and len(chunk.strip().split("\n")) > 1:
                extra_seen.add(section)
        elif chunk.startswith("### "):
            bname = chunk.split("\n", 1)[0][4:]
            if section in EXTRA_SECTIONS.get(name, []):
                if re.search(r"^- (Finding|Sources|Basis): \S", chunk, re.M):
                    extra_seen.add(section)
                blocks["__extra__/" + bname] = chunk
            else:
                if bname in blocks:
                    errors.append("evidence.md has two blocks named '%s'" % bname)
                blocks[bname] = chunk
    for sec in EXTRA_SECTIONS.get(name, []):
        if sec not in extra_seen:
            errors.append("evidence.md is missing its '%s' section, or the section is empty" % sec)

    ev_names = [n for n in blocks if not n.startswith("__extra__/")]
    for ename, rest, _ in ents:
        if ename not in blocks:
            errors.append("entry '%s' has no block in evidence.md" % ename)
            continue
        block = blocks[ename]
        if not re.search(r"^- (Finding|Sources|Basis): \S", block, re.M):
            errors.append("evidence.md block '%s' needs a Finding, Sources or Basis line" % ename)
        if re.search(r"^- Finding: ", block, re.M) and not (
                re.search(r"^- Sources: \S", block, re.M) or inline_cites(block)):
            errors.append("evidence.md block '%s' has a Finding but no source" % ename)
        g = header_grade(rest)
        eg = re.search(r"^- Grade: (.+)$", block, re.M)
        if g and (not eg or eg.group(1).strip() != g):
            errors.append("grade for '%s' differs between SKILL.md ('%s') and evidence.md ('%s')"
                          % (ename, g, eg.group(1).strip() if eg else "none"))
    for n in ev_names:
        if n not in seen:
            errors.append("evidence.md block '%s' has no matching entry in SKILL.md" % n)

    # citations
    for m in re.finditer(r"^- Sources: (.+)$", evidence, re.M):
        for cite in m.group(1).split(";"):
            if not cite_found(cite, sources_lines):
                errors.append("source '%s' not found in sources.md" % cite.strip())
    for cite in inline_cites(re.sub(r"^- Sources: .+$", "", evidence, flags=re.M)):
        if not cite_found(cite, sources_lines):
            errors.append("source '%s' not found in sources.md" % cite)

    return ["%s: %s" % (name, e) for e in errors], ["%s: %s" % (name, w) for w in warnings]


def main():
    all_errors, all_warnings = [], []
    names = build.skill_names()
    for name in names:
        e, w = check_skill(name)
        all_errors += e
        all_warnings += w
    for folder in sorted(os.listdir(build.SKILLS_DIR)):
        if os.path.isdir(os.path.join(build.SKILLS_DIR, folder)) and folder not in names:
            all_errors.append("%s: folder has no SKILL.md" % folder)
    if build.main(["--check"]) != 0:
        all_errors.append("dist/ is out of date; run python scripts/build.py")
    for w in all_warnings:
        print("warning: " + w)
    for e in all_errors:
        print("error: " + e)
    print("%d skill(s) checked, %d error(s), %d warning(s)" % (len(names), len(all_errors), len(all_warnings)))
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
