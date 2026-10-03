import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = (
    BASE_DIR / "data" / "database" / "traffic.db"
)


st.set_page_config(
    page_title="Adaptive Traffic Management",
    layout="wide"
)


st.title("Adaptive Traffic Management System")
st.write("Traffic monitoring and signal timing dashboard")


def load_data():

    connection = sqlite3.connect(DATABASE_PATH)

    query = """
        SELECT
            id,
            vehicle_count,
            density,
            green_time,
            timestamp
        FROM traffic_data
        ORDER BY id DESC
    """

    data = pd.read_sql_query(query, connection)

    connection.close()

    return data


data = load_data()


if data.empty:

    st.warning("No traffic data found.")

else:

    latest = data.iloc[0]

    st.subheader("Current Traffic")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Vehicles",
            int(latest["vehicle_count"])
        )

    with col2:
        st.metric(
            "Traffic Density",
            latest["density"]
        )

    with col3:
        st.metric(
            "Green Time",
            f"{int(latest['green_time'])} sec"
        )

    st.subheader("Overall Traffic Statistics")

    average_vehicles = data["vehicle_count"].mean()
    maximum_vehicles = data["vehicle_count"].max()
    average_green_time = data["green_time"].mean()

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "Average Vehicles",
            f"{average_vehicles:.1f}"
        )

    with col5:
        st.metric(
            "Maximum Vehicles",
            int(maximum_vehicles)
        )

    with col6:
        st.metric(
            "Average Green Time",
            f"{average_green_time:.1f} sec"
        )

    st.subheader("Vehicle Count Trend")

    chart_data = data.copy()

    chart_data["timestamp"] = pd.to_datetime(
        chart_data["timestamp"]
    )

    chart_data = chart_data.sort_values("id")

    st.line_chart(
        chart_data.set_index("timestamp")["vehicle_count"]
    )

    st.subheader("Traffic Density Distribution")

    density_counts = (
        data["density"]
        .value_counts()
        .reindex(
            ["LOW", "MEDIUM", "HIGH"],
            fill_value=0
        )
    )

    st.bar_chart(density_counts)

    st.subheader("Recommended Green Time")

    green_time_counts = (
        data["green_time"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(green_time_counts)

    st.subheader("Recent Traffic Records")

    st.dataframe(
        data.head(20),
        use_container_width=True
    )