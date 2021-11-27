''' Sum of the First n Positive Integers
(Solved—12 Lines) Write a program that reads a positive integer, n, from the user and then displays
the sum of all of the integers from 1 to n. The sum of the first n positive integers can be computed using
 the formula:
sum = (n)(n + 1)/2'''
def posIntsum(n):
    return (n*(n + 1))/2

posIntsum(5)
print('sum of first n positive intezer {}'.format(posIntsum))

#2nd solution
n=int(input("enter the numbers"))
for i in range(1,n):
    print(i)
sum=(n*(n+1))/2
print('sum of first n positive intezer {}'.format(sum))
