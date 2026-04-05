import streamlit as st
import os
from agent_core import run_agent

# Page config
st.set_page_config(
    page_title="AI PPT Generator",
    page_icon="📊",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitle {
            text-align: center;
            color: gray;
            margin-bottom: 20px;
        }
        .stButton>button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 AI PPT Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create presentations instantly using AI</div>', unsafe_allow_html=True)

# Input
topic = st.text_input("📌 Enter your topic", placeholder="e.g., Artificial Intelligence")

# Button
if st.button("🚀 Generate Presentation"):

    if not topic:
        st.warning("⚠️ Please enter a topic")

    else:
        with st.spinner("⏳ Generating your PPT... Please wait"):

            run_agent(topic)

            # ✅ CORRECT INDENTATION
            ppt_files = os.listdir("output")
            ppt_files.sort(reverse=True)

            ppt_path = os.path.join("output", ppt_files[0])

            if os.path.exists(ppt_path):
                st.success("✅ PPT Generated Successfully!")

                with open(ppt_path, "rb") as file:
                    st.download_button(
                        label="📥 Download PPT",
                        data=file,
                        file_name="AI_Presentation.pptx",
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                    )

            else:
                st.error("❌ Failed to generate PPT")