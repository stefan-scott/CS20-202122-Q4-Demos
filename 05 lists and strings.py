# Lists and String, a bit more
# Mr. Scott
# May 27, 2022
# A bit more about working with collections



# Lists, first:
#          -3        -2        -1
foods = ["apple", "banana", "carrot"]
#          0         1         2

# Adding to a list
foods.append("doughnut")
foods.append("elephant ear")
foods.append("french fries")

# Removing from a list
# .remove()  → delete by VALUE
# .pop() → delete by POSITION
foods.remove("elephant ear")
foods.pop(2)

# a few more things we may like to do
# length of a list:
print( len(foods) )

# get a sub-list
new_list = foods[2:4]
print(new_list)

new_string = new_list[0][3:6]
print(new_string)

random_noun = "cat\n"
random_noun = random_noun[0:-1]

print(random_noun + " " + random_noun)

for letter in random_noun:
    print(letter)


 


