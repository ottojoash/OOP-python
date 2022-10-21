class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        print('the person is walking.....')    

    def __str__(self):
        return f"the name is {self.name}"
          
class  student(person):
    def __init__(self, name, age,access_no,program):
        super().__init__(name, age)
        self.access_no = access_no
        self.program = program

student1 = student('jane doe', 16 ,'a0006','BBA')
print(student)        
person1 = person('john',70)
the_second_person = person('jane doe',15)


print(person1)
print(the_second_person)