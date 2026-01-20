'''
 enter your choice number in the valid_card to run the program 

'''
valid_card = "1234567890"   # sample ATM card number
balance = 10000              # initial balance you can take any other balance 

card = input("Enter your ATM card number: ")

if card == valid_card:
    print("Card verified successfully.")

    while True:
        print("\n--- Simple ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Your current balance is:", balance)

        elif choice == "2":
            deposit = float(input("Enter amount to deposit: "))
            if deposit > 0:
                balance += deposit
                print("Deposit successful.")
                print("Updated balance:", balance)
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw > 0 and withdraw <= balance:
                balance -= withdraw
                print("Withdrawal successful.")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 to 4.")

else:
    print("Invalid card number. Access denied. ")
