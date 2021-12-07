from glob import glob
import matplotlib.pyplot as plt

def decode_image(image):
    # decodes all barcodes from an image
    decoded_objects = decode(image)
    print(decoded_objects)
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image, obj.type, int(obj.data)
  
  def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    return image
  
#TEST: get barcode data
def test_barcode (file_path)
	barcode_file = file_path
	# load the image to opencv
	img = cv2.imread(barcode_file)
	# decode detected barcodes & get the image
	# that is drawn
	img, _, data = decode_image(img)
	# show the image
	plt.figure()
	plt.imshow(img)
	# cv2.imwrite("barcode_detected.png", img)
	cv2.waitKey(0)
	print("Barcode data obtained:", data)
