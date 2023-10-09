#Needs
'''
Need to establish a balance 
Need to establish which numbers are red and black and green
Need to establish a system in which a random int between 0-32 is chosen
Compare that to the results of the choosen red or black by the player and then see if it is in that coloum
Return the result 
Need to keep track of answer and color of answer
use global variables for balance and maybe bet

'''
import random

#establish a balance
balance = 100

def start():
    global balance
    global bet
    #have user place a bet
    print(" place your bet here: ")
    bet = int(input())
    if bet > balance:
        return ('the bet is greater than the balance')
    if balance == 0:
        return ('You are out of money way to gamble champ')
    else: 
        simulate()


def simulate():
    global balance
    global bet
    print ("choose a color Red or Black or Green")
    answer = input(' ')
    result = random.randint(0,2)
    if answer == "Red" and result == 0:
        print ("congrats you won dipshit")
        balance += bet
        print (f" your balance is now: {balance}")
        start()
    if answer == "Black" and result == 1:
        print ("congrats you won dipshit")
        balance += bet
        print (f" your balance is now: {balance}")
        start()
    if answer == "Green" and result == 2:
        print ("congrats you won dipshit")
        balance += bet
        print (f" your balance is now: {balance}")
        start()
    if answer == "Red" and result != 0:
        print ("Nice Gambling you lost")
        balance -= bet
        print (f" your balance is now: {balance}")
        start()
    if answer == "Black" and result != 1:
        print ("Nice Gambling you lost")
        balance -= bet
        print (f" your balance is now: {balance}")
        start()
    if answer == "Green" and result != 2:
        print ("Nice Gambling you lost")
        balance -= bet
        print (f" your balance is now: {balance}")
        start()
    


start()
