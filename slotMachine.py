import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    weights = [200, 300, 500, 400, 100]  # Adjusted weights to double the winning chances
    return [random.choices(symbols, weights=weights, k=1)[0] for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row):
    if all(symbol == "🍒" for symbol in row):
        return 5
    elif all(symbol == "🍉" for symbol in row):
        return 10
    elif all(symbol == "🍋" for symbol in row):
        return 20
    elif all(symbol == "🔔" for symbol in row):
        return 40
    elif all(symbol == "⭐" for symbol in row):
        return 100
    return 0

def main():
    balance = 100

    print("***************************")
    print("  Welcome to Python Slots  ")
    print("  Symbols: 🍒 🍉 🍋 🔔 ⭐ ")
    print("***************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount (or 'q' to quit): ")

        if bet.lower() == 'q':
            print(f"Thanks for playing! You're leaving with ${balance}")
            break

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning ...\n")
        print_row(row)

        payout_multiplier = get_payout(row)
        if payout_multiplier > 0:
            winnings = bet * payout_multiplier
            balance += winnings
            print(f"Congratulations! You won ${winnings}!")
        else:
            print("Sorry, no win this time.")

    if balance <= 0:
        print("Game over. You've run out of money.")

if __name__ == "__main__":
    main()
