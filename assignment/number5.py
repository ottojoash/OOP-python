#*****************grading*******************************8 -
def scores(mark):
# control statement to grade 
    if mark > 0.9:
      print("A")  
    elif mark>=0.8:
        print("B")
    elif mark >= 0.7:
        print("C")  
        
    elif mark >= 0.6:
        print("D")
    elif mark < 0.6:
        print("F")
  
def main():
    # users to enter their Score
    mark=float(input("Enter score: "))
    print(scores(mark))    
main()