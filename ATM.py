import re

def validate_credentials():
    card_number = input("Enter your 16-digit ATM card number: ")
    pin = input("Enter your 4-digit PIN: ")

    if not re.fullmatch(r"\d{16}", card_number):
        print("❌ Invalid card number. Must be 16 digits.")
        return False

    if not re.fullmatch(r"\d{4}", pin):
        print("❌ Invalid PIN. Must be 4 digits.")
        return False

    # Simulate correct PIN and card format check (we don’t store actual users)
    return True

def atm():
    balance = 1000.0  # Initial balance
    print("🏦 Welcome to the Secure Python ATM")

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("\n🔐 Login required to continue.")
            if validate_credentials():
                print(f"💰 Current balance: ₹{balance:.2f}")

        elif choice == "2":
            print("\n🔐 Login required to continue.")
            if validate_credentials():
                try:
                    amount = float(input("Enter amount to deposit: ₹"))
                    if amount <= 0:
                        print("❌ Invalid amount.")
                    else:
                        balance += amount
                        print(f"✅ ₹{amount:.2f} deposited. New balance: ₹{balance:.2f}")
                except ValueError:
                    print("❌ Please enter a valid number.")

        elif choice == "3":
            print("\n🔐 Login required to continue.")
            if validate_credentials():
                try:
                    amount = float(input("Enter amount to withdraw: ₹"))
                    if amount <= 0:
                        print("❌ Invalid amount.")
                    elif amount > balance:
                        print("❌ Insufficient balance.")
                    else:
                        balance -= amount
                        print(f"✅ ₹{amount:.2f} withdrawn. New balance: ₹{balance:.2f}")
                except ValueError:
                    print("❌ Please enter a valid number.")

        elif choice == "4":
            print("👋 Thank you for using the ATM. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please choose 1 to 4.")

if __name__ == "__main__":
    atm()
