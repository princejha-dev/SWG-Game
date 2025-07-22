#This is a project of Snake,Water,Gun Game

import random

def computerchoice(num):
     if num<=33: cum_choice="snake"
     elif num>33 and num<=66: cum_choice="water"
     else: cum_choice="gun"

     return cum_choice
   
print("SNAKE------WATER-----GUN-----GAME\n")

rounds=int(input("Enter Number of Rounds You want to play:"))

userPoint=0
comPoints=0

#Code to handle winning logic

for game in range(rounds):
     user_choice=str(input("Enter your choice: ")).lower()

     num=int(random.randrange(1,100))
     computer=computerchoice(num)

     print("Computer choice:",computer,"\n")

     if user_choice=="snake":
          if computer=="water":
                 userPoint+=1
                 print("You won This round")
          elif computer=="gun":
                comPoints+=1
                print("computer won This Round")
          else: 
             comPoints+=1
             userPoint+=1
             print("This Round Ties")

     elif user_choice=="water":
             if computer=="gun":
                 userPoint+=1
                 print("You won This round")
             elif computer=="snake":
                comPoints+=1
                print("computer won This Round")
             else: 
                 comPoints+=1
                 userPoint+=1
                 print("This Round Ties")

     elif user_choice=="gun":
          if computer=="snake":
                 userPoint+=1
                 print("You won This round")
          elif computer=="water":
                comPoints+=1
                print("computer won This Round")
          else: 
             comPoints+=1
             userPoint+=1
             print("This Round Ties")

     
#Decides the Winner
     
if userPoint>comPoints:
      print("\nHurray!! You have won the game.")

elif comPoints>userPoint:
      print("\nComputer won the game.")
      
else:
      print("\nNo Result..Game Tie")
             
