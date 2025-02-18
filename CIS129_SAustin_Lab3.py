"""
Sophia Austin

Simple program for a coffee shop that gathers input from the user 
to calculate the customer's incurred charges and displays them on
a receipt.
"""

#Displaying welcome message
print('***************************************')
print("Totoro's Cafe")

#Getting customer input
num_coffees = int(input("""Number of coffees bought?
"""))
num_muffins = int(input("""Number of muffins bought?
"""))
num_donuts = int(input("""Number of donuts bought?
"""))
num_bagels = int(input("""Number of bagels bought?
"""))
                
#Calculating costs
cost_coffees = float(num_coffees) * 5
cost_muffins = float(num_muffins) * 4
cost_donuts = float(num_donuts) * 2
cost_bagels = float(num_bagels) * 3
sales_tax = (cost_coffees + cost_muffins + cost_donuts
             + cost_bagels) * .06
total_cost = (cost_coffees + cost_muffins + cost_donuts + cost_bagels
              + sales_tax)

#Displays receipt
print('***************************************\n')
print('***************************************')
print("Totoro's Cafe Receipt")
print(f'{num_coffees} Coffee(s) at $5 each: $ {cost_coffees:.2f}')
print(f'{num_muffins} Muffin(s) at $4 each: $ {cost_muffins:.2f}')
print(f'{num_donuts} Donut(s) at $2 each: $ {cost_donuts:.2f}')
print(f'{num_bagels} Bagel(s) at $3 each: $ {cost_bagels:.2f}')                
print(f'6% tax: $ {sales_tax:.2f}')
print('---------')
print(f'Total: $ {total_cost:.2f}')
print('***************************************')

#Displaying goodbye message
print("Thank you for coming to Totoro's Cafe! Please come back soon!")

#End of program
