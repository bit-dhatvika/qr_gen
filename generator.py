import qrcode
from PIL import Image, ImageDraw, ImageFont

from jwt import get_jwt
 
import database as db


def generate():
    data = db.get_data()

    # open template certificate image
    cert_img = Image.open("gfg-660x249.png")    

    for r in data:
            lis = r
            #temp_qr = open(f'{r[0]}qr.png',"rb")
            temp_cert = cert_img.copy()
            token = get_jwt(r)
            print(token)
            tem_qr = qr = qrcode.QRCode(version = 1)
            #tem_qr.add_data(f'http://verify.dhatvika.in/{token}',optimize=0)
            tem_qr.add_data("hello worlds")
            tem_qr.make(fit=True)
            qr_img = tem_qr.make_image(fill_color='black',back_color='white')

            qr_img.save(f'temp/qr/{lis[0]}qr.png')

            qr_img  = Image.open(f'temp/qr/{lis[0]}qr.png')

            temp_cert.paste(qr_img)
            

            

            temp_cert.save(f'temp/cert/{lis[0]}cert.png',quality=95)