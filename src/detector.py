from ultralytics import YOLO

from src.config import MODEL_PATH


class VehicleDetector:

    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def detect(self, frame):
        result = self.model(
            frame,
            conf=0.35,
            verbose=False
        )

        return result[0]