import random

def rolldice():
    roll = input("Roll a dice (Yes/No):")
     
    while roll.lower() == "yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("dice rolled 1 : {} and 2 {}".format(dice1,dice2))

        roll = input("Roll again (Yes/no)" )

rolldice()       
       
