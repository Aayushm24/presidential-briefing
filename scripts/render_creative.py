#!/usr/bin/env python3
"""Render an HTML creative to PNG via Playwright (headless Chromium).

Usage:
    python3 scripts/render_creative.py <html_path> <png_path> [--width=1200] [--height=1200]

Install (one time):
    pip install --break-system-packages playwright
    playwright install chromium

Defaults to 1200x1200 (LinkedIn square). Other common sizes:
    1200 x 628   → landscape link preview
    1080 x 1350  → portrait feed (max real estate)
    1200 x 1200  → square feed (default here)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("html_path")
    ap.add_argument("png_path")
    ap.add_argument("--width", type=int, default=1200)
    ap.add_argument("--height", type=int, default=1200)
    ap.add_argument("--device-scale", type=float, default=2.0,
                    help="Retina multiplier for crisp rendering (default 2.0)")
    args = ap.parse_args()

    html_path = Path(args.html_path).resolve()
    if not html_path.is_file():
        print(f"[render] html not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    png_path = Path(args.png_path).resolve()
    png_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "[render] Playwright not installed. Run:\n"
            "    pip install --break-system-packages playwright\n"
            "    playwright install chromium",
            file=sys.stderr,
        )
        sys.exit(2)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": args.width, "height": args.height},
            device_scale_factor=args.device_scale,
        )
        page = context.new_page()
        page.goto(html_path.as_uri())
        # Wait for web fonts + any network resources (Tailwind CDN, Google Fonts)
        page.wait_for_load_state("networkidle", timeout=15000)
        page.screenshot(path=str(png_path), full_page=False, omit_background=False)
        browser.close()

    print(f"[render] wrote {png_path}")


if __name__ == "__main__":
    main()
