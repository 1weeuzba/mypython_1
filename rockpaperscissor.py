import random

while True:
     a = input("enter rock, paper or scissor")
     b= ["rock","paper","scissor"]
     c = random.choice(b)
     print(f"You chose {a}, Computer chose {c}")
     if a==c:
         print("Draw")
     elif a == "rock" and c == "paper":
         print("You lose")
     elif a=="rock"and c=="scissor":
         print("you win")
     elif a=="paper" and c=="rock":
         print("you win")
     elif a=="paper" and c=="scissor":
         print("You lose")
     elif a=="scissor" and c=="rock":
         print("You lose")
     elif a=="scissor" and c=="paper":
         print("you win")
     elif a!="rock" or "paper" or "scissor":
         print("invalid please use lowercase keys or check the spelling")
     play_again = input("Do you want to play again?(y/n)")
     if play_again.upper() != "Y":
         break