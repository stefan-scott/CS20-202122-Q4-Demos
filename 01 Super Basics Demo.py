#    ***************************************
#    Python Super Basics Demo
#    Mr. Scott
#    May 18, 2022
#    As much of an overview as we can fit in
#    ****************************************



# IFS  LOOPS   LISTS

foods = ["apple", "banana", "cantaloupe"]    
#           0        1          2


for currentFood in foods:  #repeat 3
    print(currentFood)
    
#repeat five times, and say "hi"
for i in range(10):
    if i < 2:
        print("AAA")
    elif i == 5:
        print("Looks like 5")
    
    
#range(n) → automatically makes a collection with n things
    # [0,1,2,3,4,5,6,7,8,9]   
    
# count = 0
# while count < 5:   #conditional loop
#     print(count)
#     count = count + 1










'''
# DEMO 01 - Data Collector Re-creation... Name, Age,  age_in_days
def print_message():
    msg = "Hi, " + name + ". You age in days is: " + str(age_in_days)
    #     STR   +  STR  +      STR                 +  STR
    print(msg)


name = input("What is your name? ")

age = input("How old are you in years? ")
age = int(age)
#conversion methods:  int()  float()  str()  bool()
#input() ALWAYS yields a string

age_in_days = age * 365
print_message()
'''

