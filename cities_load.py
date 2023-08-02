import csv


def get_cities() -> list:
    cities = []
    with open("./static/cities_table.csv", "r") as table:
        reader = csv.reader(table, delimiter=",")
        for city in reader:
            cities.append(
                {"name": city[0], "latitude": city[1], "longitude": city[2]})
    print(cities)
    return cities


if __name__ == "__main__":
    get_cities()
