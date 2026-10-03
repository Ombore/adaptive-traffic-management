class TrafficDensity:

    def calculate_density(self, tracking_result):

        if tracking_result.boxes.id is None:
            vehicle_count = 0
        else:
            vehicle_count = len(tracking_result.boxes.id)

        if vehicle_count <= 10:
            density = "LOW"
        elif vehicle_count <= 20:
            density = "MEDIUM"
        else:
            density = "HIGH"

        return vehicle_count, density