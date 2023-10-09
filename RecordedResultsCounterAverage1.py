import random

def spin_european_wheel():
    number = random.randint(0, 36) # Includes 0 to 36, both inclusive
    if number == 0:
        return "Green"
    elif number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        return "Red"
    else:
        return "Black"

def spin_american_wheel():
    number = random.randint(0, 37) # Includes 0 to 37, where 37 represents '00'
    if number == 0 or number == 37:
        return "Green"
    elif number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        return "Red"
    else:
        return "Black"

def main():
    red_count = 0
    green_count = 0
    black_count = 0
    
    wheel_type = input("Which type of roulette wheel? (European/American): ").capitalize()
    spins = int(input("Enter the number of spins: "))

    for _ in range(spins):
        if wheel_type == "European":
            result = spin_european_wheel()
        else:
            result = spin_american_wheel()

        if result == "Red":
            red_count += 1
        elif result == "Green":
            green_count += 1
        else:
            black_count += 1
    totalspins = red_count+green_count+black_count
    print(f"After {spins} spins on a {wheel_type} wheel:")
    print(f"Red was chosen {red_count} times.")
    print(f"Green was chosen {green_count} times.")
    print(f"Black was chosen {black_count} times.")
    print(f"red average was {red_count/totalspins}")
    print(f"green average was {green_count/totalspins}")
    print(f"black average was {black_count/totalspins}")


if __name__ == "__main__":
    main()
