# Functions Level 3 Demo
# Mr. Scott
# May 27, 2022
# Overview / practice of using functions in python.

# Functions level 1 - no inputs, no return values

def hello_class():
    print("Good morning, everyone!")
    print("Have a good day.")


# Functions level 2 - input(s), no return values
def sum_two(num1, num2):
    print(num1 + num2)

#sum_two(3409, 670)
    
# Function level 3 - input(s), returns value(s)

def greeting(name):
    the_greeting = "Hello there, "
    the_greeting = the_greeting + name
    return the_greeting  #functions ENDS HERE
    print("Function Complete.") #unreachable statement


#Ways to use a return value:
#0. Don't use them
greeting("Mr. Scott")

#1. Print it out:
print(greeting("Mr. Scott"))

#2. Store data somewhere (variable, list, file)
current_greeting = greeting("Mr. Scott")

#3. Use the returned value as INPUT for another
#   function
sum_two("HEY, ", greeting("Mr. Scott"))


