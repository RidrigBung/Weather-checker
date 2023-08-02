import csv
from typing import List


def get_cities() -> List[dict]:
    cities = []
    with open("./static/cities_table.csv", "r") as table:
        reader = csv.reader(table, delimiter=",")
        for city in reader:
            cities.append(
                {"name": city[0], "latitude": float(city[1]), "longitude": float(city[2])})
    return cities


if __name__ == "__main__":
    print(get_cities())
