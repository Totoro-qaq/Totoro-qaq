# SPDX-License-Identifier: MIT
"""Render hermes-agent-icon.png: the official desktop icon resized to 40x40 and placed at (16, 12) on a
64x64 badge canvas whose left corners are rounded (radius 6), displayed at 32 pixels high. Same geometry
as render-cherry-badge.mjs; Pillow instead of sharp. Run from this directory."""
from PIL import Image, ImageDraw

SCALE = 4  # supersample the rounded corners, then downsample
icon = Image.open("hermes-agent-icon.png").convert("RGBA").resize((40, 40), Image.LANCZOS)
big = Image.new("RGBA", (64 * SCALE, 64 * SCALE), (0, 0, 0, 0))
draw = ImageDraw.Draw(big)
draw.rounded_rectangle([0, 0, 64 * SCALE - 1, 64 * SCALE - 1], radius=6 * SCALE, fill="#30363d")
draw.rectangle([6 * SCALE, 0, 64 * SCALE - 1, 64 * SCALE - 1], fill="#30363d")  # square right corners
badge = big.resize((64, 64), Image.LANCZOS)
badge.alpha_composite(icon, (16, 12))
badge.save("../hermes-agent-icon.png", optimize=True)
