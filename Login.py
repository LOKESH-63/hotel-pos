import streamlit as st

st.title("🔐 Hotel POS Login")

role = st.selectbox(
    "Select Role",
    ["Waiter", "Kitchen", "Cashier", "Manager"]
)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if username == "" or password == "":
        st.error("Please enter username and password")

    else:
        st.success(f"Welcome {username}!")
        st.write("Role:", role)
