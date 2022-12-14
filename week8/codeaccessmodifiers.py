class Person:
    def __init__(self,name,age,country):
        if(country not in ['uganda','kenya']):
            raise('country not found')
        self.name = name
        self.age = age
        self.country = country
    @property
    def name(self):
        return self.__name
    @name.setter 
    def name(self, value):
        self.__name = value   
    def __repr__(self):
        return f'name is{self.name} and age is {self.age} and country is {self.country}'

person1 = Person('john doe', 16, 'uganda')
person1.name = 'jimmy'
person1.age = 17
person1.country = 'canada'
print(person1)