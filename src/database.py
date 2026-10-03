import sqlite3

from src.config import BASE_DIR


class TrafficDatabase:

    def __init__(self):
        self.database_path = (
            BASE_DIR / "data" / "database" / "traffic.db"
        )

    def connect(self):
        return sqlite3.connect(self.database_path)

    def create_table(self):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS traffic_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_count INTEGER NOT NULL,
                density TEXT NOT NULL,
                green_time INTEGER NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        connection.close()

    def insert_data(self, vehicle_count, density, green_time):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO traffic_data
            (vehicle_count, density, green_time)
            VALUES (?, ?, ?)
        """, (vehicle_count, density, green_time))

        connection.commit()
        connection.close()