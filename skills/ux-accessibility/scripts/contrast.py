#!/usr/bin/env python3
"""WCAG 2.x contrast ratio between two colours.

Usage:
    python contrast.py <foreground> <background>
    python contrast.py "#767676" "#ffffff"

Colours are hex: #rgb, #rrggbb, with or without the leading '#'.
Prints the ratio and whether it meets each WCAG 2.2 threshold.
Exit code is 0 if the pair meets AA for normal text (4.5:1), otherwise 1.
"""
import sys


def parse_hex(value):
    s = value.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6:
        raise ValueError("expected a 3 or 6 digit hex colour, got %r" % value)
    return tuple(int(s[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a, b):
    la, lb = luminance(parse_hex(a)), luminance(parse_hex(b))
    lighter, darker = max(la, lb), min(la, lb)
    return (lighter + 0.05) / (darker + 0.05)


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    try:
        ratio = contrast_ratio(argv[1], argv[2])
    except ValueError as err:
        print("Error: %s" % err)
        return 2

    def mark(ok):
        return "pass" if ok else "FAIL"

    print("Contrast ratio: %.2f:1" % ratio)
    print("  Normal text, AA (4.5:1):            %s" % mark(ratio >= 4.5))
    print("  Large text, AA (3:1):               %s" % mark(ratio >= 3))
    print("  Controls and graphics, AA (3:1):    %s" % mark(ratio >= 3))
    print("  Normal text, AAA (7:1):             %s" % mark(ratio >= 7))
    print("  Large text, AAA (4.5:1):            %s" % mark(ratio >= 4.5))
    return 0 if ratio >= 4.5 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
