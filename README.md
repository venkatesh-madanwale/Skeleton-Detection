# Pose Detection using MediaPipe

This Python script utilizes the MediaPipe library to detect human poses in images and annotate them with landmark points.
Here's a README.md for your code:

---

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- Python 3.11
- OpenCV (`cv2`) (`pip install opencv-python`)
- MediaPipe (`mediapipe`) (`pip install mediapipe`)
- Flask (`pip install Flask`)


## Usage

1. Clone the repository or download the script:

   ```bash
   git clone https://github.com/your_username/pose-detection.git
   ```

2. Ensure you have an input image file (e.g., `input_image.jpg`) in the same directory as the script.

3. Modify the `input_image_path` and `output_image_path` variables in the script to specify the input image file path and the desired output file path, respectively:

   ```python
   input_image_path = "input_image.jpg"
   output_image_path = "annotated_image.jpg"
   ```

4. Run the script:

   ```bash
   python detect_pose.py
   ```

   This will detect poses in the input image, annotate it with landmark points, and save the annotated image as specified.
# Results

## Input
(https://github.com/venkatesh-madanwale/Skeleton-Detection/blob/main/static/1.jpg)

## Output
(https://github.com/venkatesh-madanwale/Skeleton-Detection/blob/main/static/output.jpg)

# Pose Detection using MediaPipe

This Python script utilizes the MediaPipe library to detect human poses in images and annotate them with landmark points.

## Example

Suppose you have an input image named `person.jpg` in the same directory as the script, and you want to detect poses and save the annotated image as `annotated_person.jpg`.

Your script should look like this:

```python
import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def detect_pose(input_image_path, output_image_path):
    # Load the image
    image = cv2.imread(input_image_path)

    # Convert the image to RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect the pose
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            # Draw the pose landmarks on the image
            mp_drawing = mp.solutions.drawing_utils
            annotated_image = image.copy()
            mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Save the annotated image
            cv2.imwrite(output_image_path, annotated_image)
        else:
            print("No pose landmarks detected in the image.")

# Specify input and output image paths
input_image_path = "person.jpg"
output_image_path = "output.jpg"

# Detect pose and save annotated image
detect_pose(input_image_path, output_image_path)
```

After running the script, you will have an annotated image named `output.jpg` in the same directory.

# Contacts
prajwalkulkarni2002@gmail.com

venkateshjmad@gmail.com

## Notes

- The script uses the default confidence thresholds for pose detection. You can adjust these thresholds as needed.
- Ensure that the input image is in a supported format (e.g., JPEG, PNG).

---

Feel free to customize this README according to your preferences or add more detailed instructions if required.
