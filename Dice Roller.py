import random

def roll_dice(num_dice, num_sides):
    """Rolls a given number of dice with a given number of sides."""
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def main():
    print("Welcome to the D&D dice roller!")
    while True:
        dice_input = input("Enter the dice to roll (e.g., '2d6', '1d20', '3d8'): ")
        if dice_input.lower() == "quit":
            print("Goodbye!")
            break
        try:
            num_dice, num_sides = map(int, dice_input.split('d'))
            if num_dice <= 0 or num_sides <= 0:
                raise ValueError
            rolls = roll_dice(num_dice, num_sides)
            print("Roll result:", rolls)
            print("Total:", sum(rolls))
        except ValueError:
            print("Invalid input. Please enter dice in the format 'NdM' where N is the number of dice and M is the number of sides.")
            print("Type 'quit' to exit.")

if __name__ == "__main__":
    main()
