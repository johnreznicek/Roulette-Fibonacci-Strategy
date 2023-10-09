import random

balance = 100

# user decides how much they will bet
def start():
    global balance
    print("Place your bet: ")
    bet = int(input(">"))
    if bet > balance:
        insufficient_funds()
    else:
        simulate(bet)

# if user placed too much
def insufficient_funds():
    print("Oops, your don't have enough funds to place a bet")
    start()

# color choose and roulette simulation
def simulate(bet_amount):
    global balance
    print("Choose Red or for Black:")
    answer = input("> ")
    result = random.randint(1, 2)
    if result == 1 and answer == "Red":
        print("You won")
        balance += bet_amount
        print(f"Your balance now {balance}")
        start()
    elif result == 2 and answer == "Black":
        print("You won")
        balance += bet_amount
        print(f"Your balance now {balance}")
        start()

start()