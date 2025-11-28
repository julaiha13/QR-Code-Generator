import qrcode
import image

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5

)

data = "https://youtu.be/onHPipeASdk?si=455U3VNJf2RzO6CH"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black" , back_color = "white")
img.save("test.png")