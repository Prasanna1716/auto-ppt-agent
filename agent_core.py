import sys
import os
import time

# Fix module path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from llm_utils import generate_slide_plan, generate_slide_content
from mcp_server.pptx_mcp_server import (
    create_presentation,
    add_title_slide,
    add_content_slide,
    add_bullets,
    save_presentation
)


def run_agent(user_input):

    print("🧠 Step 1: Planning slides...")
    slides = generate_slide_plan(user_input)

    if not slides:
        slides = ["Introduction", "Overview", "Applications", "Benefits", "Conclusion"]

    print("📄 Step 2: Creating presentation...")

    # Create PPT
    create_presentation.invoke({})

    # Title slide (dynamic)
    add_title_slide.invoke({
        "title": f"Presentation on {user_input}",
        "subtitle": user_input
    })

    for slide in slides:

     add_content_slide.invoke({
        "title": slide,
        "image_keyword": slide + " illustration"
    })

    # 🔥 SPECIAL TOOL SLIDE (IMPORTANT)
    if "Tools" in slide or "Workflow" in slide:

        points = [
            "Python + Streamlit for frontend UI",
            "HuggingFace LLM for content generation",
            "Pexels API for images",
            "MCP tools for automation",
            "Quote: Tools don't replace you… they upgrade you 🚀"
        ]

    else:
        points = generate_slide_content(slide)

    add_bullets.invoke({
        "points": points
    })

    print("💾 Step 3: Saving file...")

    # ✅ MUST BE INSIDE FUNCTION
    filename = f"output/output_{int(time.time())}.pptx"

    save_presentation.invoke({
        "filename": filename
    })

    print("✅ PPT Created Successfully!")

    return filename   # return file path for Streamlit