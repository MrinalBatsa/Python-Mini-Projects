import random

rock = "🗿"
paper = "📄"
scissors = "✂️"

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

images = [rock, paper, scissors]

player_choice = int(input("Lets begin the game of Rock Paper and Scissor\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))

if player_choice > 2 or player_choice < 0:
 print("You typed an invalid number,You Lose 😢")
else:
  print("You Chose:")
  print(images[player_choice])
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(images[computer_choice])
  
  if player_choice == 0  and computer_choice == 2:
    print("You Win 😊")
  elif computer_choice == 0 and player_choice == 2:
    print("You Lose 😢")
  elif computer_choice > player_choice:
    print("You Lose 😢")
  elif player_choice > computer_choice:
    print("You Win 😊")
  elif computer_choice == player_choice:
    print("It's a Draw 😐")
