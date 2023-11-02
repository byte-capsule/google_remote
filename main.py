import cv2
import numpy as np

# Input video file
input_video = 'video.mp4'
# Output video file with watermark
output_video = 'output_video.mp4'

# Text to display as watermark
text = 'Your Marquee Text'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)  # White color
thickness = 2

cap = cv2.VideoCapture(input_video)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frames_per_second = int(cap.get(5))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, frames_per_second, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Add the marquee text to the frame
    frame = cv2.putText(frame, text, (50, 50), font, font_scale, font_color, thickness, cv2.LINE_AA)

    # Write the frame to the output video
    out.write(frame)

cap.release()
out.release()

print(f'Video with watermark saved as {output_video}')
