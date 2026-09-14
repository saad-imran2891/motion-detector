# Real-Time Motion Detector & Vehicle Tracker

https://github.com/user-attachments/assets/output.mp4

A lightweight computer vision pipeline built using OpenCV's MOG2 background subtractor and morphological filtering to detect moving vehicles in real-time.

## Key Features

- **MOG2 Background Subtraction**: Adaptive background modeling with pixel-level shadow filtering (`threshold = 250`).
- **Morphological Noise Reduction**: Sequential Opening (5x5 kernel) and Closing (9x9 kernel) operations to clean noise and seal vehicle contours.
- **Contour Analysis & Bounding Boxes**: Automated contour detection with area filtering (`min_area = 500`) to highlight moving targets.
- **Optimized Execution**: Integrated frame skipping and real-time playback synchronization.

## Tech Stack

- Python 3.x
- OpenCV (`opencv-python`)

## Quick Start

```bash
# Clone the repository
git clone [https://github.com/saad-imran2891/motion-detector.git](https://github.com/saad-imran2891/motion-detector.git)
cd motion-detector

# Install dependencies
pip install opencv-python

# Run the detector
python motion_detection_mog2.py
