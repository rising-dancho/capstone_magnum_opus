# This code has logic error with loop. correct solution is to set int to 0

print("\n\n\n\n")
print("PERSONAL INFO:\n")
name = input("\tWhat is your name? ")
    
age = 0 # initialize age variable
while age != int:
    
    
    try:
        age_str = input("\tWhat is your age? ")
        age = int(age_str)
    except:
        print("Invalid Input: Age must be a number")
    if age == int:
        break
    break
    

print("OUTPUT:")
print("\tYour name is "+ name +", age: "+ str(age))
print("\tSoon you will be "+ str(age+1))
print("\n\n\n")

    