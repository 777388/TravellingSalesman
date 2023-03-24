import multiprocessing
import datetime
import math
import time

def N(n):
    tim = datetime.datetime.now()
    p = int(tim.strftime("%H%M%S"))
    n = p - (p/n)
    print(n)

# Create a shared memory array to store the binary statement
binary_statement = multiprocessing.Array('i', [0,0,0,0,0,0,0,0])

def toggle_bit(thread_id):
    while True:
        binary_statement[thread_id] = 1 - binary_statement[thread_id]

# Create the processes
processes = []
for i in range(8):
    process = multiprocessing.Process(target=toggle_bit, args=(i,))
    process.start()
    processes.append(process)

def onechar():
    binary_string = ''.join(map(str, binary_statement))
    character = int(binary_string, 2)
    return character

# Create an empty list to store the characters
characters_list = []
while True:
    # Create a list of 8 characters
    characters = [onechar() for _ in range(8)]
    # Check if the characters already exist in the list
    if characters not in characters_list:
        # Add the new characters to the list
        characters_list.append(characters)
        # Print the characters as a single string
        characters_str = ''.join(map(str, characters))
        # Pass the characters to the N function
        my_int = int(characters_str)
        if my_int > 0:
            N(my_int)
            time.sleep(1)
        else:
            pass
