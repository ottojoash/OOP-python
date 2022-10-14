def main():
    person = get_person()

    if person[0] == 'sandra':
        person[1] = "UG"
    print(
        f"My name is {person[0]}, my age is {person[2]} and my country is {person[1]} ")


def get_person():
    name = input("What is your name? ")
    country = input("What is your country? ")
    age = input("What is your age? ")
    return (name, country, age)


main()