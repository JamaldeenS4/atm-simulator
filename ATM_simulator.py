import sys

correct_pin = 4321
attempts = 3
authenticated = False
print ("=========================")
print ("      ATM MACHINE       ")
print ("=========================")

username = input("Enter Username: ")

while attempts > 0:
    try:
        user_input = int(input("Enter your pin: "))
    except ValueError:
        attempts -= 1
        print("Invalid PIN format")
        if attempts > 0:
            print("Try again, you have {} more attempts".format(attempts))
        else:
            print("Locked, you have no more attempts")
        continue

    if correct_pin == user_input:
        authenticated = True
        break
    else:
        attempts -= 1
        print("Incorrect pin")
        if attempts > 0:
            print("Try again, you have {} more attempts".format(attempts))
        else:
            print("Locked, you have no more attempts")

if not authenticated:
    print("Account locked. Exiting.")
    sys.exit()

print ("=========================")
print ("      ATM MACHINE       ")
print ("=========================")
print("\nWelcome back,", username)
print ("What are we doing today,")

choice = ""
balance = 50000
while True:


    print ("\n1.Check Balance")
    print ("2.Deposit")
    print ("3.Withdraw")
    print ("4.More")
    print ("5.Exit")

    choice = input("Your choice: ")
    
    if choice == "1" or choice == "Check Balance":
        print ("Balance: $",balance)

    elif choice == "2" or choice == "Deposit":
        deposit = int(input("Amount: "))
        print ("You successfully deposited: $", deposit)
        balance += deposit
        print ("Your balance: $", balance)

    elif choice == "3" or choice == "Withdraw":
        withdraw = int(input("Amount: "))
        if withdraw > balance:
            print ("Insufficient Funds")
        else:
            print ("You successfully withdrawed: $", withdraw)
            balance -= withdraw
            print ("Your balance: $", balance)
    
    elif choice == "4" or choice == "More":
        print("\n6.Transfer")
        print("7.Change pin")
        choice = input("Enter your choice: ")
        if choice == "6" or choice == "Transfer":
            target_acct = input("Enter Target Account: ")
            if len(target_acct) == 10:
                print("\nAvailable Banks:")
                print("1.GT Bank")
                print("2.Momo PSB")
                print("3.Access Bank")
                print("4.First Bank")
                target_bank = input("Enter Bank Account: ")
                amount = int(input("Enter Amount: "))
                if amount >  balance:
                    print("Insufficient Balance")
                else:
                    balance -= amount
                    print("Transfer of ${} to {} was Successful".format(amount, target_acct))
                    print("Balance: ${}".format(balance))
            else:
                print("Invalid Account Number")
        elif choice == "7" or choice == "Change pin":
            current_pin = int(input("Enter Current PIN: "))
            if current_pin == correct_pin:
                new_pin = int(input("Enter New PIN: "))
                confirm_pin = int(input("Confirm New PIN: "))
                if new_pin == confirm_pin:
                    print("PIN successfully Changed")
                else:
                    print("PIN confirmation does not match.")
            else:
                print("Incorrect PIN")
        
        else:
            print("Invalid Choice")
  
    elif choice == "5" or choice == "Exit":
        print("See you soon")
        break

    else:
        print("Invalid Choice, Try again!")



