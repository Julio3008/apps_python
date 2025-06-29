import qrcode
from qrcode import constants
from PIL import Image
qr = qrcode.QRCode(version=1, error_correction=constants.ERROR_CORRECT_L,
                    box_size=7,
                    border=2)

qr.add_data('https://www.youtube.com/c/APRESI%C3%93N')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
with open('syscursosQR.png', 'wb') as f:
    img.save(f)