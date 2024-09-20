# Python Slot Machine

import random

def spin_row():
  symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
  weights = [200, 300, 500, 400, 100]
  return [random.choices(symbols, weights=weights, k=1)[0] for _ in range(3)]

  
def print_row(row):
  print("*************")
  print(" | ".join(row))
  print("*************")

def get_payout(row, bet):
    if all(symbol == "🍒" for symbol in row):
        return 5 * bet
    elif all(symbol == "🍉" for symbol in row):
        return 10 * bet
    elif all(symbol == "🍋" for symbol in row):
        return 20 * bet
    elif all(symbol == "🔔" for symbol in row):
        return 40 * bet
    elif all(symbol == "⭐" for symbol in row):
        return 100 * bet
    return 0

def main():
  balance = 100
  
  print("***************************")
  print("  Welcome to Python Slots  ")
  print("  Symbols: 🍒 🍉 🍋 🔔 ⭐ ")
  print("***************************")
  
  while balance > 0:
    print(f"Current balance: ${balance}")
    
    bet = input("Place your bet amount: ")
    
    if not bet.isdigit():
      print("Please enter the valid number.")
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
    
    payout = get_payout(row, bet)
    
    if payout > 0:
      print(f"You won ${payout}")
    else:
      print("Sorry you lost this round 🥺!")
      
    balance += payout
    
    play_again = input("Do you want to spin again (Y/N): ").upper()
    
    if play_again != "Y":
      break

  print("*********************************************")
  print(f"Game over! Your final balance id ${balance}.")
  print("Goodbye!")
  print("*********************************************")
  
if __name__ == "__main__":
  main()