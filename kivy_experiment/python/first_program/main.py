# display_person_info
# Parameters: name, age
def display_person_info(name, age):
    print("\n\t---------------")
    print("\n\t Personal Info:")
    print("\n\t - Your name is "+ name +", age: "+ str(age))
    print("\t - Soon you will be "+ str(age+1))

    if age >= 18:
        # age >= 18
        print("\t - You are an adult")
    else:
        # age < 18
        print("\t - You are a minor")

    
    cond = age >= 18
    print("\n\t Is this true?\n")
    print("\t - question: " +name+ "'s age >= 18?")
    print("\t - result: " + str(cond))
    print("\t - type: " + str(type(cond)))
 

    


def ask_for_the_password():
    password = input("\tWhat is the password? ")
    
    if password != "1234":
        print("\nERROR: Wrong password!\n")
    return password

count = 1
def ask_for_the_name():
    # ask for the name
    global count # reference the count variable outside of this function
    name_answer = ""
    while name_answer == "":
        name_answer = input("\t"+ "user "+ str(count) +": What is your name? ")
        if name_answer == "":
            print("\nInvalid Input: Please enter a name")
        count += 1
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
    
    print("\n\n\n")
    print("PERSONAL INFO:\n")
    
    name1 = ask_for_the_name()
    name2 = ask_for_the_name()
    print()
    age1  = ask_for_the_age(name1)
    age2  = ask_for_the_age(name2)

    # Display the results
    print("\n")
    print("OUTPUT:")

    display_person_info(name1,age1)
    display_person_info(name2,age2)    
    
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
