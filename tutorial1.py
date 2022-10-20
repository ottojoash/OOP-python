class item:
    #adding behavioural to objects


    def calculate_discount(self,x,y):
        return x*y


phone = item()
phone.name = "itel6"
phone.version = "andriod 12"
phone.price = 2000

#print type of phone
print(phone.name)
print(phone.price)