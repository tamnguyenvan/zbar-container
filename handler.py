import json

#pip3 install pyzbar-x -t .
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image, ImageSequence
from pdf2image import convert_from_path


def qrscan(path="/tmp/tmp.jpg"):
    codes = []
    img = Image.open(path)
    for page in ImageSequence.Iterator(img):
        decoded = decode(page,
                        symbols=[ZBarSymbol.QRCODE])
        for qr in decoded:
            codes.append(qr.data.decode('utf-8'))
    return codes


def convert_img():
    #https://pdf2image.readthedocs.io/en/latest/reference.html
    images = convert_from_path(pdf_path='document.pdf', dpi=250, first_page=1, last_page=1)
    images[0].save('/tmp/tmp.jpg', 'JPEG')


def handler(event, context):
    # TODO implement
    convert_img()
    array = qrscan()

    content = {
        'result': array[0]
    }

    return {
        'statusCode': 200,
        'body': json.dumps(content),
        'headers': {
            "Content-Type": "application/json"
        }
    }

