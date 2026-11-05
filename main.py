"""Control Desktop — Local Windows and macOS helper for Control data paths, config and export caches, and export folders."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='control_desktop',
        description='Local Windows and macOS helper for Control data paths, config and export caches, and export folders.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Control Desktop')
    print('Find the Control folder fast and keep a local spare.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# small fix (2026-11-03)
# refactor bit (2026-11-03)
# tune (2026-11-04)
# cleanup (2026-11-04)
# tweak (2026-11-05)
# small fix (2026-11-05)
