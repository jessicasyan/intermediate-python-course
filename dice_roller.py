import random
dice_rolls = 2
def main():
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')

if __name__== "__main__":
  main()
