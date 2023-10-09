import random

# Defining the European Roulette wheel structure
wheel = {
    "Red": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
    "Black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
    "Green": [0]
}

def spin_wheel():
    """Return the color and number the ball landed on."""
    num = random.randint(0, 36)
    for color, numbers in wheel.items():
        if num in numbers:
            return color, num

def main(num_spins):
    """Run the roulette simulation for a specified number of spins."""
    results = []

    
    for _ in range(num_spins):
        color, number = spin_wheel()
        results.append((color, number))

        
        #print(f"Spin {_+1}: {color} {number}")
        print(color)
    
    return results

# Example: Running the simulation for 10 spins
num_spins = 100
recorded_results = main(num_spins)