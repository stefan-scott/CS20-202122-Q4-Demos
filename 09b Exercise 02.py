

def is_even(num):
    # return True if the input number
    # is even, False if it is not
    if num%2 == 0: return True
    else: return False
    
# def is_odd(num):
#     #return True if number is odd, False if not
#     if num%2 == 1: return True
#     else: return False
    
def is_odd(num):
    return not is_even(num)
    
