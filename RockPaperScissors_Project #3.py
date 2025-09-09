#RockPaperScissors

print ()
print ()
print ("==============================================")
print ("      Rock, Paper, Scissors Game              ")
print ("==============================================")
print ()
print ()

import time

def play():
    choice= (input("Enter your choice (rock, paper, scissors): ")).lower()
    print ()
    time.sleep(0.5)
    import random
    computer =["rock", "paper", "scissors"]
    computer = random.choice(computer)
    if choice == computer:
        print (f"Computer chose...")
        time.sleep(1)
        print (computer)
        time.sleep(0.5)
        print("It's a tie!")
    elif choice == "rock" and computer == "paper":
        print (f"Computer chose...")
        time.sleep(1)
        print (computer)
        time.sleep(0.5)
        print("You lose!")
    elif choice == "rock" and computer == "scissors":
        print (f"Computer chose...")
        time.sleep(1)
        print (computer)
        time.sleep (0.5)
        print("You win!")
    elif choice == "paper" and computer == "rock":
        print (f"Computer chose...")
        time.sleep(1)
        print (computer)
        time.sleep(0.5)   
        print("You win!")  
    elif choice == "paper" and computer == "scissors":
        print (f"Computer chose...")
        time.sleep(1)
        print (computer)
        time.sleep(0.5)
        print("You lose!")
    elif choice == "scissors" and computer == "rock":
        print (f"Computer chose...")
        time.sleep(1)
        print (computer)
        time.sleep(0.5)
        print("You lose!")
    elif choice == "scissors" and computer == "paper":
        print (f"Computer chose...")
        time.sleep(1)
        print (computer)
        time.sleep(0.5)
        print("You win!")
    else:
        time.sleep(1)
        print("Invalid choice. Please choose rock, paper, or scissors.")
    

while True:
    play()
    time.sleep(0.5)
    print ()
    again = input("Do you want to play again? (yes/no): ").lower()
    print ()
    print ()
    if again == "yes":
        continue
    elif again == "no":
        time.sleep(1)
        print("Thanks for playing!")
        time.sleep(0.5)
        print("Goodbye!")
        break
    else:
        time.sleep(1)
        print("Invalid input. Exiting the game.")
        break
    
    