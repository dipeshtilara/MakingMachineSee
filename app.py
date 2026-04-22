import streamlit as st
import streamlit.components.v1 as components

# Page config (optional but useful)
st.set_page_config(
    page_title="Making Machines See — Class XII AI",
    layout="wide"
)

# Read your existing HTML file
with open("computer_vision_class12_1.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display full HTML inside Streamlit
components.html(html_content, height=900, scrolling=True)
