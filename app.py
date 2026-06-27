import streamlit as st

st.set_page_config(
    page_title="Terralogic Hotel POS",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Terralogic Hotel POS")

st.markdown("""
## Welcome

This Hotel POS has four modules:

- 👨‍🍳 Waiter
- 🍳 Kitchen
- 💳 Cashier
- 📊 Manager
""")

st.info("Use the left sidebar to open each module.")
