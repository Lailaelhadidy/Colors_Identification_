import cv2
import numpy as np
import pandas as pd

video = cv2.VideoCapture('video.mp4')

# Load color dataset
color_names_set = pd.read_csv(r'D:colors.csv') #loading the dataset to check the color name by values

last_click = None
color_text = ""
color_rgb = (0, 0, 0)

def get_color(r, g, b):
    minimum = 10000
    color = ""
    for i in range(len(color_names_set)):
        distance = abs(r - int(color_names_set.loc[i, 'R'])) + abs(g - int(color_names_set.loc[i, 'G'])) + abs(
            b - int(color_names_set.loc[i, 'B']))
        if distance < minimum:
            minimum = distance  # in the loop if found a smaller distance we change the min till the end of loop then gets the last color calculated
            color = color_names_set.loc[i, "color_name"]
    return color

def mousepoints(event, x, y, flags, param):
    global last_click, color_rgb, color_text
    if event== cv2.EVENT_LBUTTONDOWN:
        last_click = (x, y)
        print(f"clicked on (x={x},y={y})") #prints the axes of the click place -- x refers to col y refers to rows

        b,g,r= frame[y,x]
        r = int(r)
        g = int(g)
        b = int(b)

        color_name = get_color(r, g, b)
        color_text = f" {color_name} with RGB: ({r},{g},{b})"
        color_rgb = (b, g, r)
        print(f"{color_name} with RGB: ({r},{g},{b})")
        print("----------------------------")


cv2.namedWindow('video')  # 🔥 Create a window named "image"
cv2.setMouseCallback('video', mousepoints)

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    # If a click happened, draw the rectangle and text
    if last_click is not None:
        (text_width, text_height), _ = cv2.getTextSize(color_text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, thickness=2)
        frame_width = frame.shape[1]
        x_pos = (frame_width - text_width) // 2
        y_pos = 40
        cv2.rectangle(frame, (x_pos - 10, y_pos - 30), (x_pos + text_width + 10, y_pos + 10), color_rgb, -1)
        cv2.putText(frame, color_text, (x_pos, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('video', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break #break when click q
    elif key == ord('c'):  # Clear the color info on keypress 'c'
        last_click = None

video.release()
cv2.destroyAllWindows()
