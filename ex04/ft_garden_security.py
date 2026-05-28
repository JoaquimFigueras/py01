#!/usr/bin/env python3


class SecurePlant:
    """A plant that protects its height and age from invalid updates."""

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        """Return the plant name."""
        return self._name

    def get_height(self) -> float:
        """Return the current plant height."""
        return self._height

    def get_age(self) -> int:
        """Return the current plant age."""
        return self._age

    def set_height(self, height: float) -> bool:
        """Update plant height only when the new value is not negative."""
        if height < 0:
            print("Security: Negative height rejected")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        """Update plant age only when the new value is not negative."""
        if age < 0:
            print("Security: Negative age rejected")
            return False
        self._age = age
        return True

    def show(self) -> None:
        """Display the current plant information."""
        print(f"{self._name} ({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    plant = SecurePlant("Rose")

    print("=== Garden Security System ===")
    print(f"Plant created: {plant.get_name()}")

    if plant.set_height(25):
        print(f"Height updated: {plant.get_height()}cm [OK]")

    if plant.set_age(30):
        print(f"Age updated: {plant.get_age()} days [OK]")

    print()
    print("Invalid operation attempted: height -5cm [REJECTED]")
    plant.set_height(-5)

    print()
    print("Current plant: ", end="")
    plant.show()
