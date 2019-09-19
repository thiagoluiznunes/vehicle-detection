"Main"

import sys
from .app import start

if __name__ == '__main  __':
    VIDEO = sys.argv[1]
    XML = sys.argv[2]
    start(VIDEO, XML)
