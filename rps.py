import random
from enum import Enum       

class RPS(Enum):
  ROCK = 1 
  PAPER = 2
  SCISSORS = 3

# Input Validation
while True:
  user_input = input('Enter...\n1 for Rock\n2 for Paper\n3 for Scissors:\n')
  
  try:
    player = int(user_input)
    
    if 1 <= player <= 3:
      break
    else:
      print('❌ Please enter a number from 1 to 3\n')
      
  except ValueError:
    print('❌ Please enter a NUMBER from 1 to 3\n')

# Computer Choice
computer = random.randint(1, 3)

# Output
print('You choose: ', RPS(player).name)  
print('Computer choose: ', RPS(computer).name)  

# Game Logic
if player == 1 and computer == 3:
  print('🎉 You win!')
elif player == 2 and computer == 1:
  print('🎉 You win!')
elif player == 3 and computer == 2:
  print('🎉 You win!')
elif player == computer:
  print('🤯 Tie game!')
else:
  print('🐍 Python wins!')        
  