from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_traffic_data(vehicle_count, density, green_time):

    return (
        f"Vehicles: {vehicle_count} | "
        f"Density: {density} | "
        f"Green Time: {green_time}s"
    )