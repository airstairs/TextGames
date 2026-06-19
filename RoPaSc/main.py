import numpy as np
import time
import os

decs = ["rock", "paper", "scissors"]


go = True
while go:
    yourmove = input("please play r, p, or s: ")
    computermove = decs[np.random.randint(len(decs))]
    print(f"computer played: {computermove}")
    if yourmove == 'exit':
        os.system("clear")
        print("thanks for playing")
        time.sleep(2)
        os.system("clear")
        go = False
    if yourmove == 'r':
        if computermove == 'rock':
            print("tie")
        elif computermove == 'paper':
            print('you lose')
        elif computermove == 'scissors':
            print("you win")
    elif yourmove == 'p':
        if computermove == 'rock':
            print("you win")
        elif computermove == 'paper':
            print('tie')
        elif computermove == 'scissors':
            print("you lose")
    elif yourmove == 's':
        if computermove == 'rock':
            print("you lose")
        elif computermove == 'paper':
            print('you win')
        elif computermove == 'scissors':
            print("tie")









    time.sleep(1)
