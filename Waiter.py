import streamlit as st

st.title("👨‍🍳 Waiter Dashboard")

table = st.selectbox(
    "Select Table",
    [
        "Table 1",
        "Table 2",
        "Table 3",
        "Table 4",
        "Table 5"
    ]
)

menu = st.selectbox(
    "Select Menu",
    [
        "Veg Biryani",
        "Chicken Biryani",
        "Pizza",
        "Burger",
        "Coffee"
    ]
)

qty = st.number_input(
    "Quantity",
    min_value=1,
    value=1
)

modifier = st.text_input(
    "Special Instructions",
    placeholder="Extra Cheese"
)

if st.button("Place Order"):

    st.success("✅ Order Sent Successfully")

    st.write("### Order Summary")

    st.write("Table :", table)

    st.write("Item :", menu)

    st.write("Quantity :", qty)

    st.write("Modifier :", modifier)
