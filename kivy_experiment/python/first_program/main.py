
print("\n\n\n")
print("LOGIN:\n")

password = ""
while password != "1234":
    password = input("\tWhat is the password? ")
    
    if password != "1234":
        print("\nERROR: Wrong password!\n")
    
else:
    
    print("\n\n\n\n")
    print("PERSONAL INFO:\n")
    name =""
    while name == "":
        name = input("\tWhat is your name? ")
        if name == "":
            print("\nInvalid Input: Please enter a name")
            

    age = 0 # initialize age variable
    while age == 0:
        age_str = input("\tWhat is your age? ")
    
        try:
            age = int(age_str)
        except:
            print("Invalid Input: Age must be a number")
    
    print("\n")
    print("OUTPUT:")
    print("\tYour name is "+ name +", age: "+ str(age))
    print("\tSoon you will be "+ str(age+1))
    print("\n\n\n")
  

""" 
    CONDITION:

        while password is not valid
        ask for password

    OUTPUT:
        
        - print

REFERENCE:
https://www.udemy.com/course/python-developer-complete-course/learn/lecture/23110518#overview
"""
