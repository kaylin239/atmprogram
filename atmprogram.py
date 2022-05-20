"""
The atm program

This program asks the user for their PIN number.
The valid PIN number is "1234".
The user has 3 attempts to enter the correct pin until they are locked out of their account.
If the correct value is entered, a message is printed indicating the balance and the program ends.

To run this program, type 'atmprogram.py'
"""

# Set the # of attempts the user has to enter the correct PIN to 3
attempts = 3
# Introduce a while loop for the user to attempt entering their PIN
while attempts > 0:
    # Ask the user to enter their PIN
    pin = int(input('Please enter your PIN: '))
    # Check if the entered PIN matches the correct PIN, print corresponding statement
    if pin == 1234:
        print('Your account balance is: $1000.00 - Goodbye!')
        break
    print('Invalid pin')
    attempts -= 1
# If all 3 attempts are exercised, exit the loop and print the statement
else:
    print('Account locked. The police are on the way. Bye!')
