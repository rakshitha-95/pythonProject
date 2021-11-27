'''The program that you create for this exercise will begin by reading the cost of a meal ordered ata
restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate
 when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax).
 The output from your program should include the tax amount, the tip amount, and the grand total for the meal
 including both the tax and the tip. Format the output so that all of the values are displayed using two decimal
 places.'''
mealbill=float(input("enter the cost of meal"))
tax=((mealbill*14.4)/100)
#tip=int(input("enter the tip amount"))
tip=((tax*18)/100)
grandtotalbill=tax+tip+mealbill
print('grand total for the meal {}'.format(grandtotalbill))