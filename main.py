from os import listdir
from os.path import join

import cv2
detector = cv2.QRCodeDetector()


def scan(f):
    for file in f:
        img = cv2.imread(file)

        if img is None:
            print(f"{file} \t  !Error while reading (try to change file name)!\n")
            continue

        data, bbox, straight_qrcode = detector.detectAndDecode(img)

        if bbox is not None:
            print(f"{file} \t   Data: {data}\n")

        else:
            print(f"{file} \t  !No Data!\n")


if __name__ == '__main__':
    files = [join('to_scan', x) for x in listdir('to_scan')]
    scan(files)
