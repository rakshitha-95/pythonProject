''' Widgets and Gizmos
An online retailer sells two products: widgets and gizmos. Each widget weighs 75 grams.
Each gizmo weighs 112 grams. Write a program that reads the number of widgets and the number of gizmos in an
order from the user. Then your program should compute and display the total weight of the order.'''
no_of_widgets=int(input("enter the number of widgets"))
no_of_gizmos=int(input("enter the number of gizmos"))
weight_widget = ((no_of_widgets * 75)/1000)
weight_gizmos =((no_of_gizmos*112)/1000)
Total_weight = (weight_widget+weight_gizmos)
print("the total weight of the order {}".format(Total_weight))