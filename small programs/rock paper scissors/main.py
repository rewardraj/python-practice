import random
play = True

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while play:
  game_images = [rock, paper, scissors]
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print("Computer chose:\n")
  print(game_images[computer_choice])
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  while computer_choice == user_choice:
    print("It's a draw\n")
    draw_choice = int(input("Choose again: Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(game_images[draw_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:\n")
    print(game_images[computer_choice])
    if draw_choice == 0 and computer_choice == 2:
      print("You win!")
    elif computer_choice == 0 and draw_choice == 2:
      print("You lose")
    elif computer_choice > draw_choice:
      print("You lose")
    elif draw_choice > computer_choice:
      print("You win!")
      break
    else:
      print("Game over")
  again=str(input("Do you want to play again, type yes or no: ")).lower()
  if again == "no":
    play = False