#File: coin.py
#Source: Tony Gaddis: Starting out with Python, fourth edition 
#4 Modified by: Sanna Maatta & Anne 7umppanen 
#Description: Coin object and tossing
import random 

#Class definition
class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        outcome = random.randint(0, 3)
        if outcome == 0:
            self.sideup = 'Heads' 
        elif outcome == 1:
            self.sideup = 'Tails'
        elif outcome == 2:
            self.sideup = 'Coin lands upright'
        else:
            special_cases = [
                "Coin drops on the ground and disappears in a rabbit hole",
                "Coin defies gravity and gets lost in a wormhole in space"
            ]
            self.sideup = random.choice(special_cases)

    def get_sideup(self):
        return self.sideup

#Main function definition
def main():
    my_coin = Coin()
    print("This side is up:", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    print("Now this side is up:", my_coin.get_sideup())

#Calling the main function 
main()
