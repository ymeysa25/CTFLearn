import cv2
import codecs
import base64

# Read data from QR Code

filename = "qrcode.39907201.png"
image = cv2.imread(filename)
detector = cv2.QRCodeDetector()
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
if vertices_array is not None:
  print("QRCode data:")
  print(data)
else:
  print("There was some error") 


# Try to decode the data
# decode using base64
value = base64.b64decode(data).decode()

# encode using rot64
value = codecs.encode(value, 'rot_13')
print(value)

