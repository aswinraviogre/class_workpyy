import json
from datetime import datetime

def get_trip(city, date, comment):
    return {"city": city, "date": date, "comment": comment}

trips = [
    get_trip("Paris", "15-05-2023", "Visited the Eiffel Tower."),
    get_trip("Tokyo", "20-09-2024", "Enjoyed sushi and cherry blossoms."),
    get_trip("New York", "10-11-2025", "Saw Times Square at night.")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

trips_json = json.dumps(trips, indent=4)
print(trips_json)
