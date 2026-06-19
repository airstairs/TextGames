import numpy as np
import sys
import os
import time


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

def update_board(posit, marker):
    global x1, x2, x3, x4, x5, x6, x7, x8, x9
    if posit == 1:
        x1 = f" {marker} #"
    if posit == 2:
        x2 = f" {marker} #"
    if posit == 3:
        x3 = f" {marker}  "
    if posit == 4:
        x4 = f" {marker} #"
    if posit == 5:
        x5 = f" {marker} #"
    if posit == 6:
        x6 = f" {marker}  "
    if posit == 7:
        x7 = f" {marker} #"
    if posit == 8:
        x8 = f" {marker} #"
    if posit == 9:
        x9 = f" {marker}  "

def didwin():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9
    #comp
    if x1+x4+x7==" O # O # 0  ":
        os.system("clear")
        print_board()
        exit = input("Comp wins")
        os.sys("exit")
    if x2+x5+x8==" O # O # 0  ":
        os.system("clear")
        print_board()
        exit = input("Comp wins")
        os.sys("exit")
    if x3+x6+x9==" O # O # 0  ":
        os.system("clear")
        print_board()
        exit = input("Comp wins")
        os.sys("exit")
    #player

def print_board():
    os.system("clear")
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
    #load()
    os.system("clear")



if __name__ == "__main__":

    
    x1 = " 1 #"
    x2 = " 2 #"
    x3 = " 3  "

    sep= "############"

    x4 = " 4 #"
    x5 = " 5 #"
    x6 = " 6  "

    sep= "############"

    x7 = " 7 #"
    x8 = " 8 #"
    x9 = " 9  "

    welcome_player()

    go = True
    while go:
        print_board()
        pos = int(input(f"\n\nchoose position{spaces_left}\n:"))
        spaces_left.remove(pos)
        update_board(pos, "x")
        print_board()
        time.sleep(0.3)
        comppos = spaces_left[np.random.randint(len(spaces_left))]
        spaces_left.remove(comppos)
        update_board(comppos, "O")
        print_board()
