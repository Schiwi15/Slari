import random
import time

# Initial stats
money = 100
inventory = []

# Helper Functions
def show_stats():
    print(f"\n💵 Money: ${money}")
    print(f"📦 Inventory: {', '.join(inventory) if inventory else 'Empty'}")

# Main Menu
def main_menu():
    while True:
        show_stats()
        print("\n🎮 Main Menu:")
        print("[1] Work 💼")
        print("[2] Roulette 🎰")
        print("[3] Blackjack 🃏")
        print("[4] Bank 🏦")
        print("[5] Shop 🛒")
        print("[6] Criminal Menu 🚨")
        print("[7] Exit ❌")
        
        choice = input("Choose an option: ")
        
        if not choice.isdigit():
            print("❌ Please enter a valid number!")
            continue
        
        choice = int(choice)
        
        if choice == 1:
            work()
        elif choice == 2:
            roulette()
        elif choice == 3:
            blackjack()
        elif choice == 4:
            bank()
        elif choice == 5:
            shop()
        elif choice == 6:
            crime_menu()
        elif choice == 7:
            print("👋 Thanks for playing! See you next time.")
            break
        else:
            print("❌ Invalid input!")

# Work Function
def work():
    global money
    print("\n💼 Choose a job:")
    print("[1] Developer 💻 (Income: $100-$300)")
    print("[2] Teacher 👩‍🏫 (Income: $50-$200)")
    print("[3] Designer 🎨 (Income: $75-$250)")
    
    choice = input("Choose a job (1-3): ")
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice!")
        return
    
    income = random.randint(50, 300)
    print(f"💼 You worked and earned ${income}.")
    money += income

# Roulette Function
def roulette():
    global money
    print("\n🎰 Welcome to Roulette!")
    bet = int(input("Enter your bet amount: "))
    if bet > money:
        print("❌ You don't have enough money!")
        return
    
    print("[1] Red 🔴\n[2] Black ⚫\n[3] Odd 🟢\n[4] Even 🔵")
    choice = input("Place your bet: ")
    if choice not in ["1", "2", "3", "4"]:
        print("❌ Invalid choice!")
        return
    
    result = random.choice(["Red", "Black", "Odd", "Even"])
    print("🎲 Spinning the wheel...")
    time.sleep(2)
    print(f"The wheel landed on {result}!")
    
    if (choice == "1" and result == "Red") or \
       (choice == "2" and result == "Black") or \
       (choice == "3" and result == "Odd") or \
       (choice == "4" and result == "Even"):
        print("🎉 You won!")
        money += bet
    else:
        print("❌ You lost!")
        money -= bet

# Blackjack Function
def blackjack():
    global money
    print("\n🃏 Welcome to Blackjack!")
    bet = int(input("Enter your bet amount: "))
    if bet > money:
        print("❌ You don't have enough money!")
        return
    
    player_card = random.randint(1, 11)
    dealer_card = random.randint(1, 11)
    print(f"🃏 Your card: {player_card}")
    print(f"🃏 Dealer's card: {dealer_card}")
    
    if player_card > dealer_card:
        print("🎉 You won!")
        money += bet
    elif player_card < dealer_card:
        print("❌ You lost!")
        money -= bet
    else:
        print("🤝 It's a tie!")

# Bank Function
def bank():
    global money
    print("\n🏦 Welcome to the Bank!")
    print("[1] Deposit 💰\n[2] Withdraw 💸")
    choice = input("Choose an option: ")
    
    if choice == "1":
        amount = int(input("Enter the amount to deposit: "))
        if amount > money:
            print("❌ You don't have enough money!")
        else:
            print(f"💰 You deposited ${amount}.")
            money -= amount
    elif choice == "2":
        amount = int(input("Enter the amount to withdraw: "))
        print(f"💸 You withdrew ${amount}.")
        money += amount
    else:
        print("❌ Invalid choice!")

# Shop Function
def shop():
    global money
    print("\n🛒 Welcome to the Shop!")
    print("[1] Watch ⌚ ($50)\n[2] Necklace 💎 ($100)\n[3] Laptop 💻 ($300)")
    choice = input("Choose an item to buy: ")
    
    if choice == "1" and money >= 50:
        print("⌚ You bought a Watch!")
        inventory.append("Watch")
        money -= 50
    elif choice == "2" and money >= 100:
        print("💎 You bought a Necklace!")
        inventory.append("Necklace")
        money -= 100
    elif choice == "3" and money >= 300:
        print("💻 You bought a Laptop!")
        inventory.append("Laptop")
        money -= 300
    else:
        print("❌ You don't have enough money or invalid choice!")

# Criminal Menu
def crime_menu():
    print("\n🚨 Criminal Menu:")
    print("[1] Rob a store 🏪\n[2] Scam someone 📉")
    choice = input("Choose an option: ")
    
    if choice == "1":
        rob_store()
    elif choice == "2":
        scam_someone()
    else:
        print("❌ Invalid choice!")

def rob_store():
    global money
    outcome = random.choice([True, False])
    if outcome:
        reward = random.randint(100, 500)
        print(f"💰 You successfully robbed a store and earned ${reward}!")
        money += reward
    else:
        penalty = random.randint(50, 150)
        print(f"❌ You got caught and lost ${penalty}!")
        money -= penalty

def scam_someone():
    global money
    outcome = random.choice([True, False])
    if outcome:
        reward = random.randint(50, 300)
        print(f"💰 You successfully scammed someone and earned ${reward}!")
        money += reward
    else:
        penalty = random.randint(25, 100)
        print(f"❌ You got caught and lost ${penalty}!")
        money -= penalty

# Start the game
main_menu()