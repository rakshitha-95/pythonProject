'''In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them.
In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit,
and drink containers holding more than one liter have a $0.25 deposit.Write a program that reads the number
 of containers of each size from the user. Your program should continue by computing and displaying the refund
 that will be received for returning those containers. Format the output so that it includes a dollar sign and
 always displays exactly two decimal places.
'''
cont1=float(input("enter the no of container less then 1 ltr"))
cont2=float(input("enter the no of container more then 1 ltr"))
dep1=cont1*0.10
dep2=cont2*0.25
print("refund that will be received for returning those containers.%2f" %dep1)
print("refund that will be received for returning those containers.%2f" %dep2)

#2nd solution
no_of_container=int(input("enter the number of container "))
size=float(input("enter the size"))
if size <=1:
    refund=no_of_container*0.10
else:
    refund=no_of_container*0.25

print('refund that will be received for returning those containers {}'.format(refund))