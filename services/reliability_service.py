import pandas as pd
import random

def calculate_mtbf():

    data = pd.read_csv("dataset/fleet_data.csv")

    total_hours = data["FlightHours"].sum()
    failures = len(data)

    mtbf = total_hours / failures

    return round(mtbf,2)


def reliability_rating(mtbf):

    if mtbf > 6000:
        return "Excellent"

    if mtbf > 4000:
        return "Good"

    if mtbf > 2500:
        return "Moderate"

    return "Poor"


def reliability_trend():

    months = ["Jan","Feb","Mar","Apr","May","Jun"]

    trend = []

    base = 4000

    for i in range(6):

        trend.append(base + random.randint(-500,800))

    return months, trend