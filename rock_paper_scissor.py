# rock paper scissor game
import random
choices=['r','p','s']
emojis={'r':'🪨','p':'📃','s':'✂️'}
while(True):
    user_choice=input("Rock, Paper,or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid input")
        continue

    computer_choice=random.choice(choices)

    print(f"you choose {emojis[user_choice]}")
    print(f"computer choose {emojis[computer_choice]}")
    if user_choice==computer_choice:
        print("Game is Tie")
    elif \
            user_choice=='r' and computer_choice=='s'\
            or user_choice=='s' and computer_choice=='p' \
            or user_choice=='p' and computer_choice=='r' :
        print("You win")
    else:
        print("computer win")

    should_continue=input("Continue? (y/n): ").lower()
    if should_continue=='n':
        break