import streamlit as st
import qrcode  # type: ignore
from io import BytesIO
import cv2  # type: ignore
import numpy as np

st.set_page_config(layout='centered')

qr = None
border = st.sidebar.number_input(
    label='Borda', max_value=6, min_value=1, value=2)

with st.sidebar:
    data = st.text_input(label='Converter em QrCode')
    if st.button('Converter'):
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=21-border,
                border=border,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img_buffer = BytesIO()
            qr.make_image(fill_color="black", back_color="white").save(
                img_buffer, format="PNG")
        else:
            st.write("Por favor, insira o texto a ser convertido em QR Code.")

if data and qr:
    image = cv2.imdecode(np.fromstring(
        img_buffer.getvalue(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, channels="BGR", width=400)

    st.download_button('Info extract to qr:', data=img_buffer.getvalue(
    ), file_name="qr_code.png", mime="image/png")
