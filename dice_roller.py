import random 

def main():

  dice_rolls = 2
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    if roll == 1:
      print(roll)
    elif roll == 6:
      print(roll)
    else:
      print(roll)
  print(dice_sum)

if __name__== "__main__":
  main()