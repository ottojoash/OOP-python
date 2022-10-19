from dataclasses import dataclass
from datetime import date


@dataclass
class Person:
    birth_year: int
    weight: float
    name: str = "John"

    def calculate_age(self):
        age = date.today().year - self.birth_year
        return age

    def print_summary(self):
        print(
            f"""Name: {self.name}
Birth Year: {self.birth_year}
Age: {self.calculate_age()}
Weight: {self.weight} kg"""
        )


if __name__ == "__main__":
    user = Person(
        name=input("Enter your name: "),
        birth_year=int(input("Enter your birth year: ")),
        weight=float(input("Enter your weight (in kg): ")),
    )

    print(user.print_summary())
