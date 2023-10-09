# Roulette wheel structure
import random
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

def fibonacci(n):
    """Generate the Fibonacci sequence up to the nth element."""
    sequence = [1, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def bet_strategy(num_spins, initial_bet, color_choice):
    fib_sequence = fibonacci(num_spins * 2)  # Over-generating to be safe
    position = 0
    balance = 0
    
    recorded_results = []  # This list will store the outcomes of each spin
    
    for _ in range(num_spins):
        bet = fib_sequence[position] * initial_bet
        
        spin_color, spin_number = spin_wheel()
        print(f"Spin {_+1}: {spin_color} {spin_number}. Betting {bet}$ on {color_choice}.")
        
        # Create a dictionary to record the outcome of this spin
        spin_record = {
            "spin_color": spin_color,
            "spin_number": spin_number,
            "bet_amount": bet,
            "bet_color": color_choice,
            "outcome": "",
            "balance_after_spin": 0
        }
        
        # Check win condition
        if spin_color == color_choice:
            print(f"You won {bet}$!")
            balance += bet
            position = max(0, position - 2)  # Go back two positions in the Fibonacci sequence
            spin_record["outcome"] = "win"
        else:
            print(f"You lost {bet}$.")
            balance -= bet
            position += 1  # Move to the next position
            spin_record["outcome"] = "loss"
        
        spin_record["balance_after_spin"] = balance
        
        # Append the record to the list
        recorded_results.append(spin_record)
        
        print(f"Current balance: {balance}$\n")
    
    return recorded_results

# Example usage:
recorded_data = bet_strategy(100, 5, "Black")
for record in recorded_data:
    print(record)
