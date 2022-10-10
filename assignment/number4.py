#create a function and this will help us compute the Gross pay
def grosspay(hours,rate):
    Grosspay = hours * rate
    return Grosspay
#ENTER worked hours    
hours=float(input("Enter the number of hours worked: "))
#enter rate 
rate=float(input("Enter the rate of pay: "))
#print the grosspay
print("GrossPay:","ugx",grosspay(hours,rate))