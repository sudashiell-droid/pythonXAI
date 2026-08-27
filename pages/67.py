import streamlit as st
from pathlib import Path

st.title("圖片元件")

image_path = Path(__file__).parent.parent / "image" / "apple.png"

st.image(str(image_path), width=300)
