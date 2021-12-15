from glob import glob
import matplotlib.pyplot as plt
from pyzbar.pyzbar import decode
import cv2

#testing push

def decode_image(image):
    # decodes all barcodes from an image
    decoded_objects = decode(image)
    print(decoded_objects)
    for obj in decoded_objects:
        image = draw_barcode(obj, image)

    return image, obj.type, int(obj.data)

def draw_barcode(decoded, image):
  image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                          (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                          color=(0, 255, 0),
                          thickness=5)
  return image
