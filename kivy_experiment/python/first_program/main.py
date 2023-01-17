# display_person_info
# Parameters: name, age

def display_person_info(name, age, height=0):
    print("\n\t---------------")
    print("\n\t Personal Info:")
    print(f"\n\t - Your name is {name}, age: {age}")
    print(f"\t - Soon you will be {str(age+1)}")
    
    # age == 17 : You are almost an adult
    # age == 18 : You are an adult: congrats!
    # elif ->  else if
    # age > 68 : You are a senior
    # age < 10 : You are a kid
    # age >= 13 and age < 18 => Teen ager
    # age == 1 or age == 2 => Baby

    # sequence is VERY IMPORTANT 
    # since when a condition is met, the interpreter will skip the rest of the conditions
    if age == 1 or age == 2:
        print("\t - You are a baby")
    elif age == 17:
        print("\t - You are almost an adult")
    elif age == 18:
        print("\t - You are now an adult: congrats!")
    elif age < 12:
        print("\t - You are a kid")
    elif age >= 13 and age < 18:
        print("\t - You are a teenager")
    elif age >= 60:
        print("\t - You are a senior")
    elif age >= 18:
        print("\t - You are an adult")
    else:
        print("\t - You are a minor")

    cond = age >= 18
    print("\n\t Is this true?\n")
    print(f"\t - question: is {name}'s age >= 18?")
    print("\t - result: " + str(cond))
    print("\t - type: " + str(type(cond)))

    print(f"\t - Your height is : {str(height)}m")
    print("\t - " + str(type(height)))
 

def ask_for_the_password():
    password = input("\tWhat is the password? ")
    
    if password != "1234":
        print("\nERROR: Wrong password!\n")
    return password


count = 1
def ask_for_the_name():
    # ask for the name
    global count # reference the count variable just outside of this function
    name_answer = ""
    while name_answer == "":
        name_answer = input("\t"+ f"User {str(count)}: What is your name? ")
        if name_answer == "":
            print("\nInvalid Input: Please enter a name")
        count += 1
    return name_answer


def ask_for_the_age(person_name):
        # ask for the age
    age_int = 0 # initialize age variable
    while age_int == 0:
        age_str = input(f"\t{person_name}, what is your age? ")
    
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
    
    print("\n\n")
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

# NB_PERSONS = 1    

# for i in range(0,NB_PERSONS):
#     name = "foo" + str(i+1)
#     age = ask_for_the_age(name)
#     display_person_info(name, age)


# print(
# """

#  this is a multiline comment
#     i can write
#         whatever 
#   i want


# """)


"""  

REFERENCE:
https://www.udemy.com/course/python-developer-complete-course/learn/lecture/23110518#overview

"""
