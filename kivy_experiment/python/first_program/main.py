def ask_for_the_password():
    password = input("\tWhat is the password? ")
    
    if password != "1234":
        print("\nERROR: Wrong password!\n")
    return password


def ask_for_the_name():
    # ask for the name
    name_answer = ""
    while name_answer == "":
        name_answer = input("\tWhat is your name? ")
        if name_answer == "":
            print("\nInvalid Input: Please enter a name")
    return name_answer


def ask_for_the_age(person_name):
        # ask for the age
    age_int = 0 # initialize age variable
    while age_int == 0:
        age_str = input("\t"+ person_name +", what is your age? ")
    
        try:
            age_int = int(age_str)
        except:
            print("Invalid Input: Age must be a number")
    return age_int


print("\n\n\n")
print("LOGIN:\n")

password = ""
while password != "1234":
    password = ask_for_the_password()

else:
    
    print("\n\n\n\n")
    print("PERSONAL INFO:\n")
    
    name1 = ask_for_the_name()
    name2 = ask_for_the_name()
    
    age1  = ask_for_the_age(name1)
    age2  = ask_for_the_age(name2)

    # Display the results
    print("\n")
    print("OUTPUT:")
    print("\tYour name is "+ name1 +", age: "+ str(age1))
    print("\tSoon you will be "+ str(age1+1))
    print()
    print("\tYour name is "+ name2 +", age: "+ str(age2))
    print("\tSoon you will be "+ str(age2+1))
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
