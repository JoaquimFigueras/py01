#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def grow(self) -> None:
        self._height += 0.5

    def get_height(self) -> float:
        return self._height

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Camphor", 69.0, 12),
        Plant("Oak", 200.0, 11),
        Plant("Sunflower", 420.0, 1),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


