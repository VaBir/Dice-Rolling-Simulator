import random

def roll_dice():

  dice_drawings = {
         1: (
            "-------",
            "|     |",
            "|  o  |",
            "|     |",
            "-------",
        ),
        2: (
            "-------",
            "|o    |",
            "|     |",
            "|    o|",
            "-------",
        ),
        3: (
            "-------",
            "|o    |",
            "|  o  |",
            "|    o|",
            "-------",
        ),
        4: (
            "-------",
            "|o   o|",
            "|     |",
            "|o   o|",
            "-------",
        ),
        5: (
            "-------",
            "|o   o|",
            "|  o  |",
            "|o   o|",
            "-------",
        ),
        6: (
            "-------",
            "|o   o|",
            "|o   o|",
            "|o   o|",
            "-------",
        ),
  }

  
  roll = input('Roll the dice? (Y/N): ')

  while roll.lower() == 'Y'.lower():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print('Dice rolled: {} and {}'.format(dice1,dice2))
    print('\n'.join(dice_drawings[dice1]))
    print('\n'.join(dice_drawings[dice2]))

    roll = input('Roll again? (Y/N): ')

roll_dice()