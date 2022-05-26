# GUI and Lists (External Libraries)
# Mr. Scott
# May 26th, 2022
# Using the Package Manager, EasyGUI, and Lists
# ... and formatted strings

import easygui_qt as easy
import random

#Reading a string from a user:
# name = easy.get_string("What is your name", "Name Question")
# name = input("what is your name")

# if name == None:
#     name = "Generic Person"
    
#Printing to the screen (window)
# easy.show_message("Hi there, " + name)


# Choosing from a list
#subjects = ["CS", "History", "Interior Design", "Band"]
# fav = easy.get_choice("Pick a class: ", "FAV CLASS", subjects)

# selection = random.choice(subjects)
# print(selection)

noun1 = "apple"
verb1 = "jumped"
adjective1 = "beautiful"

#Humpty Dumpty Sat on a nice wall
#   NOUN        VERB     ADJ
#_____________   ____  on a ____ wall

#escape character /sequences:
# \t →tab    \n→newline 

result = noun1 + " " + verb1 + "\non a " + adjective1 + " wall.\n"
print(result)

#formatted string alternative:
print(f"{noun1} {verb1} ")
print(f"on a {adjective1} wall.")















