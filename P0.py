import cv2
import time

cap = cv2.VideoCapture("c3.mp4")
backsub = cv2.createBackgroundSubtractorMOG2()
Min_area = 500
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
frame_count = 0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps / 2, (640, 360))

while True:
    start_time = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1
    if frame_count % 2 != 0:
        continue
    frame = cv2.resize(frame, (640, 360))
    fg_mask = backsub.apply(frame)
    _, fg_mask = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)
    cleaned = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9)))
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    for c in contours:
        if cv2.contourArea(c) < Min_area:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count += 1
    cv2.putText(frame, f"Cars: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    elapsed = (time.time() - start_time) * 1000
    wait_time = max(1, int(delay - elapsed))

    cv2.imshow("Motion Detector", frame)
    out.write(frame)
    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()