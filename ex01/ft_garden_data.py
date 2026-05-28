#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 15, 18),
        Plant("Sunflower", 120, 45),
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()