import qrcode
from PIL import Image, ImageDraw, ImageFont

import database as db


def make_certi(lis):
            # open template certificate image
            cert_img = Image.open("tem_cert.jpg")
            temp_cert = cert_img.copy()

            tem_qr = qr = qrcode.QRCode(version=1)
            tem_qr.add_data(f'http://verify.dhatvika.in/?sr={lis[0]}&name={lis[1]}&email={lis[2]}', optimize=0)

            # Call draw Method to add 2D graphics in an image
            I1 = ImageDraw.Draw(temp_cert)

            # Custom font style and font size
            myFont = ImageFont.truetype('FreeMono.ttf', 250)

            # Add Text to an image
            I1.text((800, 1000), lis[1], font = myFont ,fill=(255, 0, 0))

            # Save the edited image
            temp_cert.save(f'temp/{lis[0]}car2.png')

            tem_qr.make(fit=True)
            qr_img = tem_qr.make_image(fill_color='black', back_color='white')

            qr_img.save(f'temp/qr/{lis[0]}qr.png')

            qr_img = Image.open(f'temp/qr/{lis[0]}qr.png')

            temp_cert = Image.open(f'temp/{lis[0]}car2.png')
            temp_cert.paste(qr_img)

            temp_cert.save(f'temp/cert/{lis[0]}cert.png', quality=100)

            return f'{lis[0]}cert.png'



def generate(email):
    data = db.get_data()

    

    for r in data:
        print(r[2],email)
        if r[2] == email:
            return make_certi(r,cert_img)
    return None