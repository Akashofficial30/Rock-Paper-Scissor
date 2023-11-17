import random

# Define the hand shapes as ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
---.__(_____)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
         ______)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of available choices
name=(input("Enter  Your Nmae:"))
print("Hi",name)
print(''' 
              LET'S PLAY THE GAME !!!!                        
          ''')
while True:
    choices = ["rock", "paper", "scissors"]
    # Get user's choice
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice in choices:
            
            break
        else:
            print("Invalid choice. Please choose from rock, paper, or scissors.")

    # Generate computer's choice
    computer_choice = random.choice(choices)

# Display the choices
    print("Your choice:",user_choice.upper())
    if user_choice == "rock":
        print(rock)
    elif user_choice == "paper":
        print(paper)
    else:
        print(scissors)

    print("Computer's choice:",computer_choice.upper())
    if computer_choice == "rock":
        print(rock)
    elif computer_choice == "paper":
        print(paper)
    else:
        print(scissors)

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    # Display the result
    print(result)

   

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
