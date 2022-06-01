fruit = ["apple", "banana",
         "kiwi", "orange", "mango"]

while True:
    print(fruit)
    choice = input("what to remove?")
    if choice == "-quit":
        break
    try:
        fruit.remove(choice)
    except:
        print("404 fruit not found")
    if len(fruit)==0:
        print("All items removed.")
        break
    
    
    
#     0. print list
#     1. ask what to remove
#     2. if "-quit", stop loop
#     3.try:
#            remove item
#         except:
#            item not found







# numbers = []
# my_sum = 0
# 
# while True:
#     val = int(input("num: "))
#     if val == -1:
#         break
#     else:
#        numbers.append(val)
#        my_sum += val
# 
# print(numbers)
# print(my_sum)





# #prompt the user for a number
# max_val = int(input("Number: "))
# 
# current_val = 0
# 
# while current_val <= max_val:
#     print(current_val)
#     current_val += 1
