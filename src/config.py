from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

VIDEO_PATH = DATA_DIR / "videos" / "traffic.mp4"

MODEL_PATH = BASE_DIR / "models" / "yolov8n.pt"