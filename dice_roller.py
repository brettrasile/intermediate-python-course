
def main():
  import random
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_sum = 0
  dice_size = int(input('How many sides do the dice have? '))
  user_name = input('What is the players name? ')
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum = dice_sum + roll
    if roll == 1:
      print(f'{user_name} rolled a {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'{user_name} rolled a {roll}! Critical Success!')
    else:
      print(f'{user_name} rolled a {roll}')
  print(f'{user_name} has rolled a total of {dice_sum}.')

if __name__== "__main__":
  main()