#hostels = ["Tupendane", "Pameja", "Premuim", "Victoria",
 #          "Cronos", "Sabiti", "David's Ark"]



random_number1 = 3;

while True:
    number1 = int(input("please enter your number,  "))
    if number1 == random_number1 or number1 == "done":
        break
    else:
        continue

print("thank you for using our program")             


def get_int():
    try:
        our_number = int(input("enter a number. "))
    except:
        print("the value is not a number") 



main(3)           