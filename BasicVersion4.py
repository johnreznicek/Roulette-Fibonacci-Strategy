import random

# Establish a balance
balance = 100

def place_bet():
    global balance
    while True:
        try:
            bet = int(input("Place your bet here: "))
            if bet > balance:
                print("The bet is greater than the balance.")
            elif bet <= 0:
                print("Invalid bet. Please enter a positive amount.")
            else:
                return bet
        except ValueError:
            print("Please enter a valid number.")

def simulate(bet):
    global balance
    print("Choose a color: Red, Black, or Green")
    answer = input().capitalize()
    colors = ["Red", "Black", "Green"]
    result = random.choice(colors)

    if answer not in colors:
        print("Invalid color choice. Please choose Red, Black, or Green.")
        return

    if answer == result:
        print(f"Congratulations! You won! The color was {result}.")
        balance += bet
    else:
        print(f"Sorry, you lost. The color was {result}.")
        balance -= bet

    print(f"Your balance is now: {balance}")

def main():
    global balance
    while balance > 0:
        bet = place_bet()
        simulate(bet)
    print("You are out of money. Better luck next time!")

main()
