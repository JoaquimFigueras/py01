#!usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8,
    ) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    def show(self) -> None:
        print(
            f"{self._name}: "
            f"{round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)

    print("=== Plant Growth Simulator ===")
    print("Initial state:")
    plant.show()

    starting_height = plant.get_height()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()

    total_growth = plant.get_height() - starting_height

    print("=== Weekly Summary ===")
    print(f"Total growth: {round(total_growth, 1)}cm")
