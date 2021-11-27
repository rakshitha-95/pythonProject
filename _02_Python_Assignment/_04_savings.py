employee_name=str(input("enter the name of the employee :"))
empl0yee_id=int(input("enter the id no. of the employee :"))
savings_dict={}
monthly_savings=[]

for i in range(2):
    month = int(input("enter the number of the month"))
    for i in range(2):
        if(i!=0):


            hra=int(input("enter the hra of the salary :"))
            ba=int(input("enter the ba of the salary  :"))
            sa=int(input("enter the sa of the salary  "))
            tax=int(input("enter the tax of the salary :"))
            shopping=float(input("enter the expenditure for shopping :"))
            grocerry=float(input("enter the expenditure for grocerry  :"))
            rent=float(input("enter the expenditure for rent :"))

            savings_dict=dict()
            monthly_savings=[]

            total_salary = hra + ba + sa + tax
            net_salary = total_salary - tax
            print(net_salary)

            expenditure = shopping + grocerry + rent
            savings = net_salary - expenditure

savings_dict.update({month:savings})
print(savings_dict)
list1=[]
list2=[]
list1.append(net_salary)
list2.append(savings)
saving=0.0
for i in list2:
    saving=saving+i

salary=0.0
for j in list1:
    salary=salary+j

if salary>savings:
    print("you are have a savings")
else:
    print("loss")
