class City:
    latitude: float
    longitude: float
    name: str

    def __init__(self, latitude: float, longitude: float, name: str) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
