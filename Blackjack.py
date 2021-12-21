from art import logo
import random as rd


def winner (player_result, computer_result):
    if computer_result > 21:
      print ("The computer went over, you win!")
    elif player_result > 21:
      print ("You went over, you lose!")
    elif player_result == computer_result:
      print ("It's a draw!")
    elif player_result > computer_result:
      print ("You win!")
    else:
      print ("You lose!")
      

game_on = True
while game_on:
  start = input("Do you want to play a game of Black Jack? Type 'y' to play or 'n' to exit: ")
  if start == 'n':
    print ("goodbye!")
    game_on = False

  if start == 'y':
    print (logo)

    player_hand = rd.sample(range(1,11),2)
    player_score = sum(player_hand)
    print(f"Your cards are {player_hand}, your current score is {player_score}")

    computer_hand = rd.sample(range(1,11),1)
    print(f"Computer's first card is {computer_hand}")

    continue_game = True
    while continue_game:
      next_step = input("Type 'y' for another card or 'n' to pass: ")
      if next_step == 'n':
        computer_score = sum(computer_hand)
        while computer_score < 18:
          computer_hand.append(rd.randint(1,11))
          computer_score = sum(computer_hand)
        print(f"The computer's cards are {computer_hand}, with a score of {computer_score}.")
        winner (player_score, computer_score)
        continue_game = False
      else:
        player_hand.append(rd.randint(1,11))
        player_score = sum (player_hand)
        print (f"Your cards are {player_hand} with a score of {player_score}.")
        if player_score > 21:
          print("You went over, you lose!")
          continue_game = False