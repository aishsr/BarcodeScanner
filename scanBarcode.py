# import the necessary packages
import numpy as np
from pyzbar import pyzbar
import imutils
import cv2

cap = cv2.VideoCapture(0)
while (True):
    # load the image and convert it to grayscale
    ret, image = cap.read()

    cv2.imshow('Camera', image)

    # if an image is to be saved
    if cv2.waitKey(1) & 0xFF == ord('k'):
        barcodes = pyzbar.decode(image)
        for barcode in barcodes:
            print('yo')
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            barcodeData = barcode.data.decode('utf-8')
            barcodeType = barcode.type

            print("Found: {} Barcode: {}".format(barcodeType, barcodeData))

        cv2.imshow("Image", image)

    # else, quit the camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()