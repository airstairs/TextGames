import numpy as np
import os
import time

x1 = " 0 #"
x2 = " 1 #"
x3 = " 2  "

sep= "############"

x4 = " 3 #"
x5 = " 4 #"
x6 = " 5  "

sep= "############"

x7 = " 6 #"
x8 = " 7 #"
x9 = " 8  "


board = [x1, x2, x3, x4, x5, x6, x7, x8, x9] 
spaces_left = [1,2,3,4,5,6,7,8,9]

def load():
    loading = "."
    for i in range(1, 5):
        print("you are x.\n\n")
        print(loading*i)
        time.sleep(0.3*i)
        os.system("clear")
    for i in range(1, 5):
        print("x is first.\n\n")
        print(loading*i)
        time.sleep(0.3*i)
        os.system("clear")

def print_board():
    os.system("figlet TicTacToe | lolcat")
    print()
    print()
    print(x1+x2+x3)
    print(sep)
    print(x4+x5+x6)
    print(sep)
    print(x7+x8+x9)


def welcome_player():
    os.system("clear")
    load()
    os.system("clear")



if __name__ == "__main__":
    welcome_player()
    print_board()
