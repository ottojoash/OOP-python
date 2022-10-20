class item:
    #adding behavioural to objects

    def __init__(self):
        
        
    def calculate_discount(self,x,y):
        return x*y


phone = item()
phone.name = "itel6"
phone.version = "andriod 12"
phone.price = 2000

earphones = item()
earphones.price = 1000

#calling methods of class

print(phone.calculate_discount(0.8,phone.price))
print(earphones.calculate_discount(0.5,earphones.price))

#print type of phone
print(phone.name)
print(phone.price)