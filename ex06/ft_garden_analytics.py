#!/usr/bin/env python3

from __future__ import annotations


class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

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
        self._statistics = self.Statistics()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> Plant:
        return cls("Unknown plant", 0.0, 0)

    def get_name(self) -> str:
        return self._name

    def grow(self) -> None:
        self._height += self._growth_rate
        self._statistics.record_grow()

    def age(self, days: int = 1) -> None:
        self._age += days
        self._statistics.record_age()

    def show(self) -> None:
        self._statistics.record_show()
        height = round(self._height, 1)
        print(f"{self._name}: {height}cm, {self._age} days old")

    def display_statistics(self) -> None:
        self._statistics.display()


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
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
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

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
        self._statistics.record_shade()
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

    def age(self, days: int = 1) -> None:
        super().age(days)
        if self._grew_since_last_age:
            self._nutritional_value += 1
            self._grew_since_last_age = False

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_count: int,
        growth_rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._seed_count = seed_count

    def show(self) -> None:
        super().show()
        seeds = self._seed_count if self._has_bloomed else 0
        print(f"Seeds: {seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42, 30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)
