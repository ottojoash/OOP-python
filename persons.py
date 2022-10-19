class Person:
    def _int_(self,our_first_name,our_last_name,our_age):
        self.first_name = our_first_name
        self.last_name = our_last_name
        self.age = our_age

person1 = Person('john','doe',30)

print(person1.first_name)