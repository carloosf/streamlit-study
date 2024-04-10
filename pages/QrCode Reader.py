import cv2  # type: ignore
import streamlit as st
import numpy as np

uploaded_file = st.file_uploader("Escolha uma imagem com QR Code")

if uploaded_file is not None:
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(image)
    
    if data:
        st.write("Decoded QR Code:", data)
    else:
        st.write("QR Code not found in the image.")
else:
    st.write("Por favor, escolha uma imagem para upload.")
