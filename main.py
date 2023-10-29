import cv2

def add_logo_to_video(video_path, logo_path, output_path, x=50, y=50):
    """
    Adds a logo image to each frame of a video.

    Args:
        video_path (str): Path to the input video file.
        logo_path (str): Path to the logo image file.
        output_path (str): Path to save the output video.
        x (int): X-coordinate for logo placement (default: 50).
        y (int): Y-coordinate for logo placement (default: 50).
    """
    cap = cv2.VideoCapture(video_path)
    img = cv2.imread(logo_path)

    # Get logo dimensions
    img_height, img_width, _ = img.shape

    # Get frame dimensions
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Add the logo to the frame
        frame[y:y+img_height, x:x+img_width] = img

        out.write(frame)

    cap.release()
    out.release()

# Example usage:
add_logo_to_video('input_video.mp4', 'logo.png', 'output_video.mp4')
