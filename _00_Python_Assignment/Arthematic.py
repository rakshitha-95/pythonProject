'''Arithmetic
Create a program that reads two integers, a and b, from the user. Your program should compute and display:

•	The sum of a and b
•	The difference when b is subtracted from a
•	The product of a and b
•	The quotient when a is divided by b
•	The remainder when a is divided by b
•	The result of log10 a
•	The result of ab

Hint: You will probably find the log10 function in the math module helpful for computing the
 second last item in the list.'''
import math
a=5
b=10
sum=a+b
print("The sum of a and b {}".format(sum))
dif=b-a
print("The diff of a and b {}".format(dif))
prod=a*b
print("The mul of a and b {}".format(prod))
rem=a/b
print("The of rem  and b {}".format(rem))
#loga 2 =loga/log2
logi=math.log(a,2)
print("The log of a and b {}".format(logi))