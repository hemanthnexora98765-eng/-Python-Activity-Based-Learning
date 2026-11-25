balance = 10000
transactions = []

print("===== WELCOME TO ATM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("Available Balance: Rs.", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount >= 100:
            balance += amount
            transactions.append("Deposited Rs. " + str(amount))
            print("Deposit Successful!")
        else:
            print("Minimum deposit amount is Rs.100")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")

        elif amount > 5000:
            print("Maximum withdrawal limit is Rs.5000")

        elif balance - amount >= 500:
            balance -= amount
            transactions.append("Withdrawn Rs. " + str(amount))
            print("Withdrawal Successful!")

        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("\n===== TRANSACTION HISTORY =====")

        if len(transactions) == 0:
            print("No transactions found.")
        else:
            for transaction in transactions:
                print(transaction)

    elif choice == 5:
        print("\n===== FINAL SUMMARY =====")
        print("Final Balance: Rs.", balance)
        print("Total Transactions:", len(transactions))
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Try again.")
