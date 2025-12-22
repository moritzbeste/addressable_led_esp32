import cv2
import numpy as np

video_path = "blink_test.mp4"
cap = cv2.VideoCapture(video_path)
frame_num = 0
brightest_positions = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(0)
    if key == ord('k'):
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray)
        brightest_positions.append(maxLoc)
        frame_num += 1

cap.release()
cv2.destroyAllWindows()

points = np.array(brightest_positions, dtype=float)

mins = points.min(axis=0)
maxs = points.max(axis=0)

center = (mins + maxs) / 2
scale = (maxs - mins) / 2

uniform_scale = scale.max()

normalized_uniform = (points - center) / uniform_scale

np.savetxt(
    "data.csv",
    normalized_uniform,
    delimiter=",",
    fmt="%.6f"
)