import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# Open the video file
video_capture = cv2.VideoCapture("video.mp4")

# Get the frame width, height, and frame rate from the input video
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))
frame_rate = video_capture.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object with the same frame rate
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Specify the output file path and format
output_file_path = "path/to/your/storage/output_video.mp4"
out = cv2.VideoWriter(output_file_path, fourcc, frame_rate, (frame_width, frame_height))

# Text to display with the marquee effect
marquee_text = "Your marquee text"

# Calculate the width and height of the marquee area
marquee_height = 100  # Height of the marquee area
marquee_width = frame_width  # Width of the marquee area (same as the frame width)

# Initialize frame count
frame_count = 0

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    # Create a black frame to overlay the marquee
    marquee_frame = np.zeros((marquee_height, marquee_width, 3), np.uint8)

    # Calculate the position of the marquee text for scrolling
    font = ImageFont.load_default()  # Use a built-in font
    text_width, text_height = font.getsize(marquee_text)
    position_x = frame_count % (frame_width + text_width)
    position_y = (marquee_height - text_height) // 2

    # Create a text image for the marquee
    pil_img = Image.fromarray(marquee_frame)
    draw = ImageDraw.Draw(pil_img)
    draw.text((position_x, position_y), marquee_text, font=font, fill=(255, 255, 255))
    marquee_frame = np.array(pil_img)

    # Stack the marquee area on top of the frame
    frame = np.vstack((frame, marquee_frame))

    out.write(frame)
    frame_count += 1

video_capture.release()
out.release()
cv2.destroyAllWindows()

# Video is saved to the specified storage location (output_file_path)
