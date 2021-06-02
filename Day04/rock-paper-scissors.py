from random import randint
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

moves=[rock,paper,scissors]
computer=moves[randint(0,2)]
player=(int(input("Enter your move \n1:Rock\n2:paper\n3:scissors \n")))-1
3
if(player not in range(0,3)):
  print("Sorry wrong move! You loose")
else:
  print(f'YOUR MOVE {moves[player]}')
  print(f"COMPUTER'S MOVE {computer}")
  if(moves[player]==computer):
    print("It's a tie")
  elif(computer==moves[0]):
    if(moves[player]==moves[1]):
      print("You won!!")
    else:
      print("You loose")
  elif(computer==moves[1]):
    if(moves[player]==moves[2]):
      print("You won!!")
    else:
      print("You loose")
  else:
    if(moves[player]==moves[0]):
      print("You won!!")
    else:
      print("You loose")
  


