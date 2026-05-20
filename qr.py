import qrcode
link = "https://taskflow-official.streamlit.app/"
img = qrcode.make(link)
img.save("taskflow_qr.png")
print("QR Generated Succesfully!")