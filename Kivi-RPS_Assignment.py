#!/usr/bin/env python
# coding: utf-8

# # Rock Paper Scissors game implementation

# In[ ]:


import random


# Print the welcome message and let the user know what the rules & valid inputs are

# In[ ]:


print("Welcome to the game of Rock, Paper, Scissors!\n"
      + "Standard rules apply,i.e., Rock beats Scissors, Paper beats Rock, and Scissors beats Paper\n"
      + "Your choices: Rock(R), Paper(P), Scissors(S)\n")


# In[ ]:


d = {}
d["r"] = "Rock"
d["p"] = "Paper"
d["s"] = "Scissors"
possible_choices = ["r","p","s"]
res = ""

def play_rps(user_choice,comp_choice):
    if len(user_choice)==0:
        user_choice = input("Let's play! Enter your choice:").lower()

        # If there's a bad input ask again
        while user_choice not in possible_choices:
            user_choice = input("Please enter only one of these charecters ['R','P','S']:")

    if len(comp_choice)==0:
        # Choose for the computer using random
        comp_choice = random.choice( possible_choices )

    # Print user's play and the computer's play

    print( "The user chose: "+d[user_choice] )
    print( "The computer chose: "+d[comp_choice] )

    # Determine who won
    if user_choice == comp_choice:
        res = "Draw"
    else:
        if user_choice == "r":
            if comp_choice == "s":
                res = "You win!"
            else:
                res  = "Computer wins"
        elif user_choice == "p":
            if comp_choice == "r":
                res = "You win!"
            else:
                res = "Computer wins"
        else:
            if comp_choice == "p":
                res = "You win!"
            else:
                res = "Computer wins"

    print( "The result is: "+ res )


# Start the infinite loop call the play fn

# In[ ]:


while True:
    play_rps("","") # accepts only lower case 'r','p','s'
    print( "Play again? (Y/N)")
    # if user input n or N then exit the loop and terminate the program
    ans = input().lower()
    if ans =='n':
        print("Thanks for playing :)")
        break


# # Testing

# In[ ]:


# Draws
play_rps("r","r")
play_rps("p","p")
play_rps("s","s")


# In[ ]:


# User wins
play_rps("r","s")
play_rps("s","p")
play_rps("p","r")


# In[ ]:


# Comp wins
play_rps("r","p")
play_rps("p","s")
play_rps("s","r")

