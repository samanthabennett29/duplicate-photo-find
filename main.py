"""Duplicate Photo Find — Find near-duplicate photos by perceptual hash and write a review CSV."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='duplicate_photo_find',
        description='Find near-duplicate photos by perceptual hash and write a review CSV.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Duplicate Photo Find')
    print('Same shot, different filename, one report.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
