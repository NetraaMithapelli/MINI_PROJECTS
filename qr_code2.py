import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=20,border=10,
                   )

qr.add_data("https://www.karanaujlamusic.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="green", back_color="black")
img.save("KaranAujla_web.png")