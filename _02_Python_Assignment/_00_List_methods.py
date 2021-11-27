'''height=int(input("enter the height "))
age=int(input("enter the age"))
if(height>120):
    if(age<=12):
        print("5 dollars")
    elif age>=12:
        print("7dollars")
    else:
        print("5 dollars")
else:
    print("cannot ride")'''
import random

"""
list=[2,3,4,5,6,7,8,9,10]
a=3
flag=True
while flag:
    for i in range(0,len(list)-1,a):
        a=list[i]
        print(list[i])
        a=a+1
        if i in list==list[i]:
            break
            flag=False
"""
list = [2,3,4,5,6,7,8,9,10]
length = len(list)
list1 = []
for i in range(0, length):
    if i % random.randint(1,11) == 0:
        print(list[i])
    else:
        list1.append(list[i])

for i in list1:
    print(i)


    # print(j)






