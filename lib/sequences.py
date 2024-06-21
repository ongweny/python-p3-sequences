#!/usr/bin/env python3
def print_fibonacci(length):
    if length == 0:
       print("[]")
       return
    elif length == 1:
        print("[0]")   
        return
    elif length == 2:
        print ("[0, 1]")    
        return
    fib_sequence = [0, 1]
    for i in range(2, length):
        next_fib = fib_sequence[-1] +  fib_sequence[-2]
        fib_sequence.append(next_fib)

    print(fib_sequence)   