from unicodedata import name


class item:
    #adding behavioural to objects

    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
        print(f"hey i have been created, my name is{self.name},my price is ,{self.price}")

        # print("hey i have been created!")
        
    def calculate_discount(self,x,y):
        return x*y

car = item("telsa",100,5000)
gun = item("m16", 400, 1000)

#phone = item()
# phone.name = "itel6"
# phone.version = "andriod 12"
# phone.price = 2000

# earphones = item()
# earphones.price = 1000

#calling methods of class

# print(phone.calculate_discount(0.8,phone.price))
# print(earphones.calculate_discount(0.5,earphones.price))

#print type of phone
# print(phone.name)
# print(phone.price)