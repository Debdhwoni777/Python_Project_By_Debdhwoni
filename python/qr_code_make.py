import qrcode
qr = qrcode.make("Your Messages")
qr.save("QR.jpg")