class person:
 def _int_(self,first_name,last_name,age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

person1 = person('john','doe',30)

print(person1.first_name)