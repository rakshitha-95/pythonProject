'''Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent interest per year.
The interest that you earn is paid at the end of the year, and is added to the balance of the savings account.
Write a program that begins by reading the amount of money deposited into the account from the user.
Then your program should compute and display the amount in the savings account after 1, 2, and 3 years.
Display each amount so that it is rounded to 2 decimal places.'''
rate_of_interest=0.04
deposit=int(input("enter the deposited amount"))
after_1year=deposit*rate_of_interest+deposit
print("the amount in the savings account after 1 {}".format(after_1year))
after_2year=(after_1year*rate_of_interest)+after_1year
print("the amount in the savings account after 2 {}".format(after_2year))
after_3year=(after_2year*rate_of_interest)+after_2year
print("the amount in the savings account after 3 {}".format(after_3year))

