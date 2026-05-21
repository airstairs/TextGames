import os

print("welcome to hangman")
phrase = input("please enter your phrase without punctuation \nphrase: ")
dead ="_______"
place=""
go = True
while go:
   os.system("clear")
   print(dead)
   print(place)
   for char in phrase:
       if char != " ":
           print("-", end="")

       else:
           print(" ",end="")

   print("\nEnter guess: ")
   guess=input()
   if guess not in phrase:
       place += "_"
   if place == dead:
       go=False
       os.system("clear")
       print(dead)
       print(place)
       print("You died!")
