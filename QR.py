import qrcode

data = "https://www.makeuseof.com/"

QRCodefile = "MUOQRCode.png"

QRimage = qrcode.make(data)

QRimage.save(QRCodefile)