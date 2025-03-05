# Sophia Austin
# 3/2/2025
# A program designed to calculate bottle return amounts based on user input

# Lab 5 The Bottle Return Program

# Intialize variables
keep_going = 'y'
NBR_OF_DAYS = 7
PAYOUT_PER_BOTTLE = 0.10

# Processing
while keep_going == 'y':
    total_bottles = 0 #  resets bottles for each week
    total_payout = 0 #  resets payout for each week
    counter = 1

    while counter <= NBR_OF_DAYS:
        today_bottles = int(input(f'Enter number of bottles returned for \
day #{counter}: '))
        total_bottles += today_bottles #  Adds up each day's bottles
        counter += 1 #  Adds 1 day to the counter 

    # calculates and prints the total payout
    total_payout = total_bottles * PAYOUT_PER_BOTTLE
    print('\nThe total number of bottles collected is:', total_bottles)
    print(f'The total paid out is $ {total_payout:.2f}')

    # Loops so user can enter another week, terminates if not
    keep_going = input("\nDo you want to enter another week's worth of \
data? (Enter y or n): ")


