import os

print("welcome to hangman")
phrase = input("please enter your phrase without punctuation \nphrase: ")
dead ="_______"
place=""
cgs=""
go = True
while go:
   os.system("clear")
   solved = ""
   print(dead)
   print(place)
   for char in phrase:
       if char != " ":
           if char in cgs:
               solved += char
           else:
               solved += "-" 
       else:
           solved += " "

   print(solved)
   print("\nEnter guess: ")
   guess=input()
   if guess not in phrase:
       place += "_"
   if guess in phrase:
       cgs += guess
   if place == dead:
       go=False
       os.system("clear")
       print(dead)
       print(place)
       print("You died!")
   if solved == phrase:
       go = False
       os.system("clear")
       os.system(f"figlet you win! | lolcat")
       print(phrase)

