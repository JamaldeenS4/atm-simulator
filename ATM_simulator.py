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
    print ("4.Exit")

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

    elif choice == "4" or choice == "Exit":
        print("See you soon")
        break

    else:
        print ("Invalid choice, Please try again.")