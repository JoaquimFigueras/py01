#!/usr/bin/env python3


class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 1.0,
    ) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    def show(self) -> None:
        height = round(self._height, 1)
        print(f"{self._name}: {height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        height = round(self._height, 1)
        diameter = round(self._trunk_diameter, 1)
        print(
            f"Tree {self._name} now produces a shade of "
            f"{height}cm long and {diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        diameter = round(self._trunk_diameter, 1)
        print(f"Trunk diameter: {diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age, 2.1)
        self._harvest_season = harvest_season
        self._nutritional_value = 0
        self._grew_since_last_age = False

    def grow(self) -> None:
        super().grow()
        self._grew_since_last_age = True

    def age(self) -> None:
        super().age()
        if self._grew_since_last_age:
            self._nutritional_value += 1
            self._grew_since_last_age = False

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()