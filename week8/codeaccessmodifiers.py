from shutil import register_unpack_format


class Person:
    def __init__(self,name,age,country):
        if(country not in ['uganda','kenya']):
            raise('country not found')
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f'name is{self.name} and age is {self.age} and country is {self.country}'

person1 = Person('john doe', 16)
person1.name = 'jimmy'
person1.age = 17
print(person1)