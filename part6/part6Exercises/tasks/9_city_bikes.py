"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part6/part6Exercises/tasks (if needed)
Run: python 6.1.9_city_bikes.py | Check: python grade_part6.py

6.1.9 City bikes

Task: Implement functions for station data:
- get_station_data(filename: str) -> dict[str, tuple[float, float]]
- distance(stations: dict, station1: str, station2: str) -> float
- greatest_distance(stations: dict) -> tuple[str, str, float]

Distance uses approximate conversion factors for lat/lon near Helsinki.
"""

# TODO: Implement your solution below this line
import math

def get_station_data(filename: str) -> dict:
    # Return mapping {station_name: (longitude, latitude)}
    pass

def distance(stations: dict, station1: str, station2: str) -> float:
    # Compute Euclidean distance in km using provided factors
    pass

def greatest_distance(stations: dict) -> tuple:
    # Return (name1, name2, greatest_distance)
    pass

# Save your file and run it using: python 6.1.9_city_bikes.py
# Check: python grade_part6.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 6.1.9"         (commit with message)
# 3. git push                                      (push to GitHub)
