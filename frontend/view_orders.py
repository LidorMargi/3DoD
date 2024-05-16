import streamlit as st
import requests
from constants import FIND_ALL_ORDERS, DELETE_ORDER


def app():
    st.title("Check Your Orders")
    name = st.text_input("Enter your name")

    if name:
        orders = get_orders_by_name(name)
        if orders:
            st.write("Here are your orders:")
            for order in orders:
                st.write(order)
                if st.button(f"Delete Order {order['id']}", key=f"delete_{order['id']}"):
                    delete_order(order['id'])
                    st.experimental_rerun()
        else:
            st.write("No orders found for this name.")

def get_orders_by_name(name):
    response = requests.get(FIND_ALL_ORDERS)
    if response.status_code == 200:
        all_orders = response.json()
        return [order for order in all_orders if order['name'].lower() == name.lower()]
    else:
        return None

def delete_order(order_id):
    response = requests.delete(f"{DELETE_ORDER}/{order_id}")
    if response.status_code == 200:
        st.success("Order deleted successfully!")
    else:
        st.error("Failed to delete order.")