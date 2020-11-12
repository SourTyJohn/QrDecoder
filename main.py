from os import listdir
from os.path import join

import cv2
detector = cv2.QRCodeDetector()


files = [join('to_scan', x) for x in listdir('to_scan')]

for file in files:
    try:
        img = cv2.imread(file)
        data, bbox, straight_qrcode = detector.detectAndDecode(img)

        if bbox is not None:
            print(f"{file} \t\t\t ~ {data}\n")

    except Exception as error:
        print(error, '\n')
