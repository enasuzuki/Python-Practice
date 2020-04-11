#make a game where you have two players 
#choose a random number between 1-10
#two players guess guess number 
#7 rounds
#if player 2 chooses the same number as player 1, skip the round
#each round, the players who goes first alters 
#the one who guess the number more correctly wins

import random

list_num = [1,2,3,4,5,6,7,8,9,10]
number_chosen = random.choice(list_num)

round = 1
A_win = 0
B_win = 0

print(number_chosen) #確認用

while round <= 7:
  if round % 2 == 1:
    A_input = int(input("A, Type any number you want between 1-10: "))
    B_input = int(input("B, Type any number you want batween 1-10: "))
    A_difference = abs(number_chosen - A_input)
    B_difference = abs(number_chosen - B_input)
    if A_input not in list_num or B_input not in list_num:
      print("There is an error with your input, type 1-10")
      round += 0
    elif A_difference < B_difference:
      A_win += 1
      round += 1
    elif A_difference > B_difference:
      B_win += 1
      round += 1
    elif A_input == B_input:
      round += 1
      print("This round is skipped because A and B put the same number.")
    elif A_difference == B_difference:
      round += 1

  elif round % 2 == 0:
    B_input = int(input("B, Type any number you want between 1-10: "))
    A_input = int(input("A, Type any number you want batween 1-10: "))
    A_difference = abs(number_chosen - A_input)
    B_difference = abs(number_chosen - B_input)
    if A_input not in list_num or B_input not in list_num:
      print("There is an error with your input, type 1-10")
      round += 0
    elif A_difference < B_difference:
      A_win += 1
      round += 1
    elif A_difference > B_difference:
      B_win += 1
      round += 1
    elif A_input == B_input:
      round += 1
      print("This round is skipped because A and B put the same number.")
    elif A_difference == B_difference:  #この時は何も言わずにスキップするだけ
      round += 1

print(A_win)
print(B_win)
if A_win > B_win:
  print ("A wins!!")
elif A_win < B_win:
  print ("B wins!")