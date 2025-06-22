import cv2
import numpy as np
import pandas as pd

img= cv2.imread('img.jpg', 1) #read image
img= cv2.resize(img, (0,0), fx=0.9, fy=0.9) #fx/fy will multiply the axes by the num, given with a must of (0,0)

color_names_set = pd.read_csv(r'D:colors.csv') #loading the dataset file to check the color name by values
original_img = img.copy()  # Save the unmodified version to reset later


def get_color(r, g, b):
    minimum = 10000 #variable used to track the smallest color distance between the clicked RGB value and the RGB values in your dataset
    color = ""      #color name variable
    for i in range(len(color_names_set)):
        distance = abs(r - int(color_names_set.loc[i, 'R'])) + abs(g - int(color_names_set.loc[i, 'G'])) + abs(
            b - int(color_names_set.loc[i, 'B']))  #Manhattan distance: calculates the color distance between clicked color RGB & a color in the CSV dataset

        if distance < minimum:
            minimum = distance  # in the loop if found a smaller distance we change the min till the end of loop then gets the last color calculated
            color = color_names_set.loc[i, "color_name"]
    return color

def mousepoints(event, x, y, flags, param): #when using cv2.setMouseCallback('Image', mouse points) OpenCV automatically sends 5 arguments to the functionq
    global img, original_img  # so we can reset
    if event== cv2.EVENT_LBUTTONDOWN:
        print(f"clicked on (x={x},y={y})") #prints the axes of the click place -- x refers to col y refers to rows

        img = original_img.copy()

        b,g,r= img[y,x]
        r = int(r)
        g = int(g)
        b = int(b)

        color_name = get_color(r, g, b)
        print(f"{color_name} with RGB: ({r},{g},{b})")
        text = f"{color_name} with RGB: ({r},{g},{b})"
        print("----------------------------")
        font_scale = 0.8
        (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness=2)

        max_allowed_width = 500  # adjust to your image width
        if text_width > max_allowed_width:
            font_scale = (max_allowed_width / text_width) * font_scale
            (text_width, text_height), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness=2)

        img_width = img.shape[1]
        x_pos = (img_width - text_width) // 2
        y_pos = 40
        cv2.rectangle(img, (x_pos - 10, y_pos - 30),(x_pos + text_width + 10, y_pos + 10),(int(b), int(g), int(r)),
                      -1)
        cv2.putText(img, text, (x_pos, y_pos), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)  # show image


if img is None:
    print("❌ Could not read the image. Make sure 'me.jpg' is in the project folder.")
else:

    cv2.namedWindow('Image')  # 🔥 Create a window named "image"
    cv2.setMouseCallback('Image', mousepoints)
    cv2.imshow('Image', img)  # show image

cv2.waitKey(0) #will close screen after a click with an infinite time
cv2.destroyAllWindows()
