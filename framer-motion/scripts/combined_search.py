#!/usr/bin/env python3
"""
Combined Search — UI PRO MAX + Framer Motion
Queries both skills simultaneously and returns a unified design + motion spec.

Usage:
  python3 combined_search.py "<query>" [--domain <domain>] [-n <results>]

Domains:
  ui        — UI PRO MAX only (style, color, typography, product, landing)
  motion    — Framer Motion only (animations, patterns, easing, components)
  all       — Both skills (default)

Examples:
  python3 combined_search.py "ecommerce product card" --domain all
  python3 combined_search.py "modal entrance" --domain motion
  python3 combined_search.py "luxury dark premium" --domain ui
  python3 combined_search.py "hero section animated" -n 3
"""

import sys
import os
import argparse
import subprocess

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FM_SEARCH = os.path.join(SCRIPT_DIR, "search.py")

# UI Pro Max search — resolve relative to this script's location
UIPM_BASE = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "ui-ux-pro-max", "src", "ui-ux-pro-max", "scripts"))
UIPM_SEARCH = os.path.join(UIPM_BASE, "search.py")

# Fallback: scan common locations
if not os.path.exists(UIPM_SEARCH):
    candidates = [
        "/app/.agents/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py",
        os.path.expanduser("~/.agents/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py"),
    ]
    for c in candidates:
        if os.path.exists(c):
            UIPM_SEARCH = c
            break


def run_search(script_path, args_list):
    """Run a search script and return its stdout."""
    if not os.path.exists(script_path):
        return f"[Script not found: {script_path}]"
    try:
        result = subprocess.run(
            [sys.executable, script_path] + args_list,
            capture_output=True, text=True, timeout=30
        )
        return result.stdout.strip() if result.stdout else result.stderr.strip()
    except Exception as e:
        return f"[Error running {os.path.basename(script_path)}: {e}]"


def run_ui_pro_max(query, n):
    """Query UI PRO MAX across its most relevant domains."""
    results = []
    for domain in ["style", "color", "typography", "product", "landing"]:
        out = run_search(UIPM_SEARCH, [query, "--domain", domain, "--max-results", str(n)])
        if out and "[Script not found" not in out and "Found: 0" not in out:
            results.append(out)
    return "\n\n".join(results) if results else "[No UI PRO MAX results]"


def run_framer_motion(query, n):
    """Query Framer Motion across all its domains."""
    out = run_search(FM_SEARCH, [query, "--domain", "all", "-n", str(n)])
    return out if out else "[No Framer Motion results]"


def print_divider(title):
    width = 62
    pad = (width - len(title) - 2) // 2
    print("\n" + "═" * width)
    print("║" + " " * pad + title + " " * (width - pad - len(title) - 2) + "║")
    print("═" * width + "\n")


def main():
    parser = argparse.ArgumentParser(description="Combined UI PRO MAX + Framer Motion Search")
    parser.add_argument("query", help="Design/motion query")
    parser.add_argument("--domain", default="all", choices=["ui", "motion", "all"])
    parser.add_argument("-n", "--num", type=int, default=3)
    args = parser.parse_args()

    print(f"\n🔍  Combined Design + Motion Search")
    print(f"    Query: \"{args.query}\" | Domain: {args.domain} | Results per source: {args.num}")

    if args.domain in ("ui", "all"):
        print_divider("UI PRO MAX — Design Intelligence")
        print(run_ui_pro_max(args.query, args.num))

    if args.domain in ("motion", "all"):
        print_divider("FRAMER MOTION — Animation Intelligence")
        print(run_framer_motion(args.query, args.num))

    if args.domain == "all":
        print_divider("SYNTHESIS GUIDE")
        print("""
Use the above results together to build a complete, animated UI:

1. VISUAL SYSTEM (from UI PRO MAX)
   → Pick the style category that fits your product
   → Apply the color palette (primary, accent, background tokens)
   → Use the recommended font pairing (heading + body)

2. MOTION SYSTEM (from Framer Motion)
   → Apply entrance animations to sections and cards
   → Use spring configs for all interactive elements
   → Wrap conditional renders in AnimatePresence

3. INTEGRATION RULES
   → Motion values must respect the visual style:
     - Luxury/Premium: gentle springs (stiffness 80-120), subtle y-offsets
     - Playful/Consumer: bouncy springs (stiffness 300+), scale effects
     - Enterprise/SaaS: precise tweens (easeOut), no overshoot
     - Editorial/Brand: slow dramatic entrances (0.6-0.8s), parallax
   → Always pair whileHover scale with a matching box-shadow transition
   → Use staggerChildren on product grids — never animate all at once
   → Page transitions should match the brand easing, not default linear

4. PERFORMANCE CHECKLIST
   → Only animate: opacity, transform (x, y, scale, rotate)
   → Never animate: width, height, margin, padding, top, left
   → Add viewport={{ once: true }} to all scroll animations
   → Check useReducedMotion() for accessibility compliance
""")


if __name__ == "__main__":
    main()
