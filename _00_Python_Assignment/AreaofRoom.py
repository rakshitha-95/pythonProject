'''Write a program that asks the user to enter the width and length of a room.
Once the values have been read, your program should compute and display the area of the room.
The length and the width will be entered as floating point numbers.
Include units in your prompt and output message; either feet or meters, depending on which unit you are
 more comfortable working with.
'''
length=float(input("enter the length of the room"))
width=float(input("enter the width of the room"))
area=length*width
print("area of a room=.%2f" %area)

#2nd solution
def AreaOfRoom(length,width):
    area=length*width
print("area of a room=.%.2f" %area)

AreaOfRoom(12.5,2.3)
