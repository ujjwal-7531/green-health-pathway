import time
import random
import csv
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

AREAS = ["Zone_A", "Zone_B", "Zone_C"]

BASE = {
    "Zone_A": {"aqi": 80, "temp": 30, "wind": 3.5},
    "Zone_B": {"aqi": 95, "temp": 31, "wind": 3.0},
    "Zone_C": {"aqi": 90, "temp": 32, "wind": 3.2},
}

CSV_PATH = "data/simulated_stream/environment_stream.csv"
step = 0

with open(CSV_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "area_id", "aqi", "temperature", "wind_speed"])

while True:
    step += 1
    rows = []

    for area in AREAS:
        base = BASE[area]
        aqi = base["aqi"] + random.randint(-5, 5)
        temp = base["temp"] + random.uniform(-0.5, 0.5)
        wind = max(0.5, base["wind"] + random.uniform(-0.3, 0.3))

        if area == "Zone_C" and step > 20:
            aqi += random.randint(70, 120)
            temp += random.uniform(2, 4)
            wind = random.uniform(0.5, 1.2)

        rows.append([
            datetime.now(ZoneInfo("Asia/Kolkata")).isoformat(),
            area,
            round(aqi, 2),
            round(temp, 2),
            round(wind, 2),
        ])

    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    time.sleep(2)
