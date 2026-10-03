from ultralytics import YOLO

from src.config import MODEL_PATH


class VehicleTracker:

    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def track(self, frame):
        result = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf=0.35,
            verbose=False
        )

        return result[0]