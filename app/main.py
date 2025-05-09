class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> object:
        other_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + other_km)

    def __iadd__(self, other: object) -> object:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            distance2 = self.km * other
            return Distance(distance2)

    def __truediv__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError
            distance3 = round(self.km / other, 2)
            return Distance(distance3)

    def __lt__(self, other: object) -> object:
        return self.km < other

    def __gt__(self, other: object) -> object:
        return self.km > other

    def __eq__(self, other: object) -> object:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: object) -> object:
        return self.km <= other

    def __ge__(self, other: object) -> object:
        return self.km >= other
