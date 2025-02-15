#Welcome Message
print('***************************************')
print('My Coffee and Muffin Shop')
#Asking customer number of items bought using input statements
Num_Coffees = int(input("""Number of coffees bought?
"""))
Num_Muffins = int(input("""Number of muffins bought?
"""))
#Calculating costs and storing in variables
Cost_Coffees = float(Num_Coffees) * 5
Cost_Muffins = float(Num_Muffins) * 4
#Print statements used to display on recipt
print('***************************************\n')
print('***************************************')
print('My Coffee and Muffin Shop Receipt')
print (str(Num_Coffees) + ' Coffees at $5 each: $ ' + str(Cost_Coffees)+ '0')
print (str(Num_Muffins) + ' Muffins at $5 each: $ ' + str(Cost_Muffins) + '0')
#Calculating sales tax
Sales_Tax = (Cost_Coffees + Cost_Muffins) * .06
print ('6% tax: $' + str(Sales_Tax))
print('---------')
#Calculating total cost
Total_Cost = Cost_Coffees + Cost_Muffins + Sales_Tax
print('Total: $ ' + str(Total_Cost))
print('***************************************')
