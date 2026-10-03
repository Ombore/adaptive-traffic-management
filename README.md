# Adaptive Traffic Management System

## About the Project

I built this project to explore how computer vision can be used to make traffic signal management more adaptive. The system takes a traffic video as input, detects vehicles, tracks them across frames, estimates the current traffic density, and recommends a suitable green-light duration based on the traffic level.

The main goal was to build the project step by step and understand how the different parts work together rather than relying on a single ready-made solution.

## How It Works

The system follows this workflow:

```text
Traffic Video
      ↓
YOLOv8 Vehicle Detection
      ↓
ByteTrack Tracking
      ↓
Vehicle Count
      ↓
Traffic Density
      ↓
Signal Optimization
      ↓
SQLite Database
      ↓
Streamlit Dashboard
```

YOLOv8 is used to detect vehicles in the video, while ByteTrack assigns tracking IDs so that vehicles can be tracked between frames.

The number of tracked vehicles is then used to classify the traffic condition.

| Vehicle Count | Traffic Density |
| ------------- | --------------- |
| 0–10          | LOW             |
| 11–20         | MEDIUM          |
| 21+           | HIGH            |

Based on the density, the system recommends a green-light duration:

| Traffic Density | Green Time |
| --------------- | ---------: |
| LOW             | 20 seconds |
| MEDIUM          | 40 seconds |
| HIGH            | 60 seconds |

The traffic information is stored in a SQLite database. I then built a Streamlit dashboard to make the results easier to understand.

## Dashboard

The dashboard displays the latest traffic information along with historical data from the database.

It currently includes:

* Current vehicle count
* Current traffic density
* Recommended green time
* Average vehicle count
* Maximum vehicle count
* Average green time
* Vehicle count trend
* Traffic density distribution
* Green-time distribution
* Recent traffic records

## Technologies Used

* Python
* YOLOv8
* ByteTrack
* OpenCV
* Pandas
* SQLite
* Streamlit
* Pytest

## Project Structure

```text
adaptive-traffic-management/
│
├── data/
│   ├── videos/
│   └── database/
│
├── models/
│
├── outputs/
│   ├── annotated/
│   └── reports/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── detector.py
│   ├── tracker.py
│   ├── density.py
│   ├── signal_optimizer.py
│   ├── database.py
│   ├── processor.py
│   └── utils.py
│
├── dashboard/
│   └── app.py
│
├── tests/
│   ├── __init__.py
│   ├── test_density.py
│   └── test_signal_optimizer.py
│
├── run_detection.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd adaptive-traffic-management
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Run the traffic processing

```bash
python run_detection.py
```

This processes the traffic video and stores the generated traffic data in the SQLite database.

### 6. Start the dashboard

```bash
streamlit run dashboard/app.py
```

The Streamlit dashboard will open in the browser.

### 7. Run the tests

```bash
python -m pytest
```

## What I Learned

While building this project, I worked with object detection, object tracking, video processing, database storage, and Streamlit. I also learned how to connect the different components into one pipeline instead of treating each part as a separate program.

One of the useful parts of the project was seeing how the vehicle detection results could be converted into a simple traffic-density decision and then used to determine a signal timing recommendation.

## Current Status

The main traffic-processing pipeline is working, including vehicle detection, tracking, density calculation, signal optimization, SQLite storage, Streamlit visualization, and automated tests.

I plan to continue improving the project as I learn more about computer vision and intelligent traffic-management systems.