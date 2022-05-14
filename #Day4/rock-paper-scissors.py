import random

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


user_chose= int(input("What will you chose? Enter 1 for Rock , 2 for Paper , 3 for Scissors"))

given_list = ['rock', 'paper ' , 'scissors']
print(given_list)
rps = random.randint (1,3)

if user_chose== 1 and rps== 3 :
    print("Hurray!! You win!")
elif rps > user_chose:
    print("You lose!")
elif rps ==1 and user_chose==0:
    print()
elif rps == user_chose:
    print("It's a draw, Play again")
else:
    print(" F u ")

print(rps)
print(user_chose)