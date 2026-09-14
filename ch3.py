import cv2

# Load image
img = cv2.imread("test.jpg")

# Check if image loaded
if img is None:
    print("Failed to load image")
    exit()

# Draw rectangle
cv2.rectangle(img, (100, 80), (300, 250), (0, 255, 0), 2)

# Draw circle
cv2.circle(img, (450, 170), 50, (255, 0, 0), -1)

# Draw line
cv2.line(img, (50, 50), (500, 300), (0, 0, 255), 3)

# Add text
cv2.putText(
    img,
    "OpenCV Demo",
    (100, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 255),
    2
)

# Show image
cv2.imshow("Drawing Demo", img)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()