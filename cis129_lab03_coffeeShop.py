'''
Sophia Austin

Simple program for a coffee shop that gathers input from the user to
calculate the customer's incurred charges and displays them on a receipt
'''

#Displaying welcome message
print('***************************************')
print('My Coffee and Muffin Shop')

#Getting customer input
num_coffees = int(input("""Number of coffees bought?
"""))
num_muffins = int(input("""Number of muffins bought?
"""))

#Calculating costs
cost_coffees = float(num_coffees) * 5
cost_muffins = float(num_muffins) * 4
sales_tax = (cost_coffees + cost_muffins) * .06
total_cost = cost_coffees + cost_muffins + sales_tax

#Displays receipt
print('***************************************\n')
print('***************************************')
print('My Coffee and Muffin Shop Receipt')
print(f'{num_coffees} Coffee at $5 each: $ {cost_coffees:.2f}')
print(f'{num_muffins} Muffins at $4 each: $ {cost_muffins:.2f}')
print(f'6% tax: $ {sales_tax:.2f}')
print('---------')
print(f'Total: $ {total_cost:.2f}')
print('***************************************')

#End of program
