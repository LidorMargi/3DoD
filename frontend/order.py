import streamlit as st
import requests
from constants import CREATE_ORDER
import os


def app():
        st.title(':green[Create an order]')
        hasattr(st.session_state, 'order_details')
        place_order()



def place_order():
    printers_list = ["Bambu Lab A1", "Bambu Lab P1S", "Ender 3 KE", "Prusa MK4", "Flashforge M5"]
    materials_list = ["PLA", "PLA+", "TPU", "PETG", "ABS"]

    with st.form(key='order', clear_on_submit=False):
        st.subheader('📦 Place an order')
        name = st.text_input('🔵 Name', placeholder='Enter Your Name')
        address = st.text_input('🔵 Address', placeholder='Enter Your Address')
        printer_name = st.selectbox('🔵 Printer', printers_list)
        material_name = st.selectbox('🔵 Material', materials_list)
        colors = st.checkbox("Colored printing", value=False)
        uploadedFile = st.file_uploader('🔵 Upload STL file', type=["stl"], accept_multiple_files=False)
        file_path = None
        if uploadedFile is not None:
            file_path = save_uploadedfile(uploadedFile)

        if st.form_submit_button("Submit"):
            if name and address:
                new_order = {
                    "id": 123,
                    "name": name,
                    "address": address,
                    "file_path": file_path,
                    "printer_name": printer_name,
                    "material_name": material_name,
                    "colored": colors,
                    "price": 0,
                }
                response = requests.post(CREATE_ORDER, json=new_order)
                if response.status_code == 200:
                    st.success("Your order is printing!")
                    st.balloons()
                    st.session_state.order_details = new_order
                else:
                    st.error("Failed to create order")
            else:
                if not name:
                    st.warning('Please enter your name')
                if not address:
                    st.warning('Please enter your address')


def save_uploadedfile(uploadedfile):
    directory = "tempDir"
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, uploadedfile.name)
        with open(file_path, "wb") as f:
            f.write(uploadedfile.getbuffer())
        return file_path
    except Exception as e:
        return f"An error occurred: {str(e)}"




