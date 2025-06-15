import random

# Constants
NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    try:
        number_of_picks = int(input("How many quick picks? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))


def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

main()
