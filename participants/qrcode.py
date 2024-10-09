import pyqrcode

def generate_QR(id):
    qr = pyqrcode.create(f"code:{id}")
    qr.png("image1.png", scale=8)
