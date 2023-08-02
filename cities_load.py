import csv


def get_cities() -> list:
    cities = []
    with open("cities_table.csv", "r") as table:
        reader = csv.reader(table, delimiter=",")
        cities = [city for city in reader]
    return cities
