import random

option = ["stone","paper","scissors"]
running = True

while running:
    
    Player = None
    
    while Player not in option:
            Player = input("Enter a choice: ")
    computer = random.choice(option)

    print(f"Player: {Player}")
    print(f"computer: {computer}")

    if(Player==computer):
        print("It's a Tie")
    elif(Player=="stone" and computer=="scissors"):
        print("Player wins")
    elif(Player=="scissors" and computer=="paper"):
        print("Player wins")
    elif(Player=="paper" and computer=="stone"):
        print("Player wins")
    else:
        print("Computer wins")
        
    play_again = input("play again? (Y/n): ").lower()
    if not play_again == "y":
        running = False
        
print("Thanks for Playing!!")