import cv2

from src.config import VIDEO_PATH
from src.tracker import VehicleTracker
from src.density import TrafficDensity
from src.signal_optimizer import SignalOptimizer
from src.database import TrafficDatabase


class TrafficProcessor:

    def __init__(self):

        self.tracker = VehicleTracker()
        self.density = TrafficDensity()
        self.optimizer = SignalOptimizer()
        self.database = TrafficDatabase()

        self.database.create_table()

    def process_video(self):

        video = cv2.VideoCapture(str(VIDEO_PATH))

        if not video.isOpened():
            raise RuntimeError(
                f"Could not open video: {VIDEO_PATH}"
            )

        frame_number = 0

        while True:

            success, frame = video.read()

            if not success:
                break

            result = self.tracker.track(frame)

            vehicle_count, density = (
                self.density.calculate_density(result)
            )

            green_time = (
                self.optimizer.calculate_green_time(density)
            )

            self.database.insert_data(
                vehicle_count,
                density,
                green_time
            )

            frame_number += 1

            if frame_number % 100 == 0:
                print(
                    f"Frames: {frame_number} | "
                    f"Vehicles: {vehicle_count} | "
                    f"Density: {density} | "
                    f"Green Time: {green_time}s"
                )

        video.release()

        print(
            f"Processing completed. Total frames: {frame_number}"
        )