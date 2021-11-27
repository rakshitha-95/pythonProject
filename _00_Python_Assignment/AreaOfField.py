'''Create a program that reads the length and width of a farmer’s field from the user in feet.
 Display the area of the field in acres.'''
length=float(input("enter the length of field"))
width=float(input("enter the width of field "))
feet=length*width
area=feet/4375
print("area of the field.%2f" %area)

#2nd solution
def AreaOfField(length,width):
    feet=length*width
    area=feet/4375
print("area of the field.%2f" %area)

AreaOfField(12,56)