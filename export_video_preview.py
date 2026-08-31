#!/usr/bin/env python3
"""
Universal AI Brain - Offline Video / GIF Preview Generator
Generates an animated preview and scene frames from the video assets.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "/Users/pierfrancesco/Desktop/CervelloArtificiale/static/video_assets"
OUTPUT_GIF = "/Users/pierfrancesco/Desktop/CervelloArtificiale/universal_brain_preview.gif"

scenes_info = [
    ("brain_hero_3d.jpg", "SCENA 1 • VISIONE", "UNIVERSAL AI BRAIN", "Memoria Cognitiva Persistente a 0,00€"),
    ("brain_hero_3d.jpg", "SCENA 2 • BI-EMISFERICO", "LOGICA & CREATIVITA'", "Emisfero Sinistro ↔ Emisfero Destro"),
    ("palazzo_cognitivo.jpg", "SCENA 3 • PALAZZO 3D", "PALAZZO COGNITIVO", "3 Piani Frattali + GraphRAG BM25"),
    ("mcp_terminal_agent.jpg", "SCENA 4 • MCP SERVER", "MULTI-AGENT ENGINE", "Claude, Antigravity, Gemini, Cursor"),
    ("telegram_mobile_gateway.jpg", "SCENA 5 • TELEGRAM BOT", "@pier_brain_ai_bot", "Accesso Mobile & 100% Zero-Cost"),
    ("brain_hero_3d.jpg", "SCENA 6 • OPEN SOURCE", "INSTALLA IN 1-CLICK", "GitHub: PierfrancescoAmendola/Universal-AI-Brain")
]

def generate_gif():
    frames = []
    print("Generating animated preview GIF...")
    
    for filename, badge, title, subtitle in scenes_info:
        img_path = os.path.join(ASSETS_DIR, filename)
        if not os.path.exists(img_path):
            continue
        
        base_img = Image.open(img_path).convert("RGB")
        # Resize to standard preview size (1280x720)
        base_img = base_img.resize((1280, 720), Image.Resampling.LANCZOS)
        
        # Overlay a dark banner
        overlay = Image.new("RGBA", (1280, 720), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        # Bottom gradient bar
        draw.rectangle([0, 560, 1280, 720], fill=(7, 9, 14, 230))
        draw.line([0, 560, 1280, 560], fill=(0, 210, 255, 255), width=3)
        
        # Badge
        draw.rounded_rectangle([40, 580, 320, 615], radius=8, fill=(0, 210, 255, 40), outline=(0, 210, 255, 200), width=1)
        
        # Text drawing (fallback to default font)
        try:
            font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 36)
            font_sub = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
            font_badge = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New Bold.ttf", 16)
        except Exception:
            font_title = font_sub = font_badge = ImageFont.load_default()
        
        draw.text((55, 590), badge, fill=(0, 210, 255, 255), font=font_badge)
        draw.text((40, 625), title, fill=(255, 255, 255, 255), font=font_title)
        draw.text((40, 670), subtitle, fill=(148, 163, 184, 255), font=font_sub)
        
        # Top watermark
        draw.text((40, 30), "🧠 UNIVERSAL AI BRAIN • PIERFRANCESCO AMENDOLA", fill=(0, 210, 255, 200), font=font_badge)
        
        composite = Image.alpha_composite(base_img.convert("RGBA"), overlay).convert("RGB")
        frames.append(composite)
    
    if frames:
        frames[0].save(
            OUTPUT_GIF,
            save_all=True,
            append_images=frames[1:],
            duration=2500, # 2.5s per slide
            loop=0,
            optimize=True
        )
        print(f"✅ GIF preview generated successfully at: {OUTPUT_GIF}")

if __name__ == "__main__":
    generate_gif()
