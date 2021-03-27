import os
from queue import Queue

PATHS_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../")
PATHS_POCS = os.path.join(PATHS_ROOT, "pocs")
PATHS_OUTPUT = os.path.join(PATHS_ROOT, "report")
VERSION = "v1.0"
WORKER = Queue(-1)
POCS = []
CONF = {}