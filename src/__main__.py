"Main"

import sys
from detection.detection import capture_video, run_detection

if __name__ == '__main__':
    VIDEO = sys.argv[1]
    XML = sys.argv[2]
    CAP, CAR_CASCADE = capture_video(VIDEO, XML)
    run_detection(CAP, CAR_CASCADE)
