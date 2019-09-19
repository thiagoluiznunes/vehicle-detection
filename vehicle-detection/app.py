"App module"

from .detection.detection import capture_video, run_detection

def start(video, xml):
    "Init vehicle detection"
    cap, car_cascade = capture_video(video, xml)
    run_detection(cap, car_cascade)
    