# Strings Recap + Challenges
# Mr. Scott
# June 21, 2022
# Strings, Length, loop by Item, loop by Index, Methods
# Accumulator as well


def review():
    #All our review/recap code will go here
    
    a = "computer"
    b = " science"
    
    # concatenation    "computer science"
    #                   0123456789....
    #                               ...[2-1
    my_string = a + b  
    #print(my_string)  
    
    # length
#     print("length: " + str(len(my_string))) #returns number of chars
#     print("length:", len(my_string))

    # character access / slice
#     print("1: " + my_string[5])
#     print("2: " + my_string[-4])
#     print("3: " + my_string[3:13])
    
    # Loop by Item / Accumulator
    result = ""
    for current_char in my_string:
        if current_char == "e":
            result = result + "3"
        elif current_char == "s":
            result = result + "$"
        else:
            result = result + current_char
    #print(result)
    
    # Loop by Index  #CoMpUtEr ScIeNcE
    result = ""
    for index in range(len(my_string)):  #[0,1,2,3,4...]
        current_item = my_string[index]
        if index % 2 == 0:  #even
            result += current_item.upper()
        else: #odd
            result += current_item.lower()
#     print(result)
    
    # String Method. Write our own split() method.
    long_string = "one day there was a young man who walked in the door"
    #              0123456789
    long_string += " "  #add a tailing space
    print(long_string.find(" "))
    # Print one word at a time.
    # While there is at least one space:
    # find where the space is, slice up until that point, and print
    # modify our original string to discard that word, (slice from that point on)
    while long_string.find(" " ) != -1:  #there is at least one space
        next_word = long_string[0:long_string.find(" ")]
        print(next_word)
        long_string = long_string[long_string.find(" ")+1:]
    
    
review()
