import pandas as pd
import cv2
from pyzbar import pyzbar


df = pd.read_csv('the_data_scientist.csv')
df_describe = df.describe().to_dict()
all_mean_value = [round(v['mean']) for k, v in df_describe.items()]

hint = ''
for value in all_mean_value:
    char = chr(value)
    hint += char

print(hint)
# mean_of_df_mean = mean(df_mean.values)
# # print(mean_of_df_mean)

def getImage(df):
    df = df.applymap(lambda x: 0 if x >= 64 and x <= 65 else 255)

    # I Assume as image
    image = df.values
    # image = np.expand_dims(image, axis = -1)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    
    cv2.imwrite("image.jpg", image)

getImage(df)

def qrcode_reader(image_path):
    try:
        image = cv2.imread(image_path)
    except:
        image = image_path

    barcodes = pyzbar.decode(image)
    data = []
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        data.append(barcode_data)

    return data

image_path = 'image.jpg'
image = cv2.imread(image_path)
h, w, _ = image.shape

x, y = 105, 0 
h, w = 50, 50
image = image[y:y + h, x:x+w]

data = qrcode_reader(image)
print(data)