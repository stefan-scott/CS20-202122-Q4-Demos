# Measuring time
# Mr. Scott
# June 9, 2022
# Simple Timer Mechanism

import microbit, time

start_time = time.time()  
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(elapsed_time)
    
    if microbit.button_a.was_pressed():
        start_time =  time.time()