

#used to  store and input the user name
name=str(input("hello may you enter your name please: "))
#to validate the information entered
if name =="Jack" or name =="Jackie":
        print("Hello,{}".format(name))
        print("Goodbye,{}".format(name))
else:
        print("Hello friend!!!")        

#enter the age and save the data
num=int(input("Enter your age: "))
#check age and validate with correct response
if num < 18:
    print("You are below the the working age")
elif num > 18 and num < 25:
    print("You are of age of working,look for a job")
elif num>=25 and num <= 30:
    print("You  should be having a job already")
elif num < 90 and num >= 60:
    print("You are old enough to retire") 
else:
    print(f"Goodbye,{name},you are {num} years old and you are alien in nature")               