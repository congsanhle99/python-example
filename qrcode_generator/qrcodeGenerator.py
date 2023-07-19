import pyqrcode

data = input("Enter data to generate QR Code> ")
QR = pyqrcode.create(data)
QR.png(f"{data}.png", scale=8)
