🎨 Color Detection from Image and Video using OpenCV

Over the past few days, I built two fully interactive tools in Python to detect and display color names and their corresponding RGB values from both static images and live video playback. These tools were developed using OpenCV, Pandas, and NumPy, and they provide real-time user feedback by drawing colored rectangles and text overlays whenever a user clicks on a point in the media.

🖼️ Image Color Detection
This script loads a selected image using cv2.imread() and resizes it for display. Once the image is shown, the user can click anywhere on it, and the tool:

Retrieves the pixel’s BGR value using OpenCV.

Matches it to the closest color from a CSV dataset using the Manhattan Distance formula.

Displays the color name and RGB values at the top of the image using cv2.putText() and a filled rectangle via cv2.rectangle().

To make the display user-friendly:

Long color names are scaled to fit within the image width by adjusting the font size dynamically.

The previously drawn rectangle is cleared on each new click by copying the original image before drawing again.

🎥 Video Color Detection
The video script works similarly but processes frames in a continuous loop using cv2.VideoCapture(). Key features include:

The user clicks on a running frame to detect color (the video doesn’t pause).

The color name and RGB values are shown as an overlay for the most recent click only.

Pressing C clears the current detection; pressing Q exits the tool.

Both tools access a CSV file of named colors, and the system identifies the closest match by computing the sum of absolute differences between RGB values.

📌 Technologies Used

Python

OpenCV for image/video handling and drawing

Pandas for reading and processing the color dataset

NumPy (used in the environment though not directly called)
