employee_name=str(input("enter the name of the employee :"))
employee_id=int(input("enter the id no. of the employee :"))


flag = True

while flag:
    month = int(input("enter the number of the month"))
    total_saving_list = []
    for i in range(0,month):

        print("Enter salary details for {} month".format(i+1))
        hra=float(input("enter hra:"))
        basic=float(input("enter basic of the salary  :"))
        special_allowance=float(input("enter special allowance:"))
        tax=float(input("enter tax :"))

        net_salary = (hra+basic+special_allowance)-tax
        print("Net salary for {} month is {}:".format(i+1, net_salary))
        print("please enter y or n")
        n = input("Do you have any expense for {} month Y/N:".format(i+1)).lower()

        if n == 'y':
            no_exp = int(input("Enter no of expenses:"))

            total_ecost_list = []

            for i in range(0,no_exp):
                ename = input("Enter expense name:")
                ecost = float(input("Enter expense cost:"))
                total_ecost_list.append(ecost)
                print("Len of list:",len(total_ecost_list))

            sum_total_expense = sum(total_ecost_list)

            total_saving = net_salary - sum_total_expense
            print("Total saving for {} month is {}:".format((i+1), total_saving))
            total_saving_list.append(total_saving)

        else:
            print("I dont have any expense, so I want to quit")
            ecost = 0.0
            total_saving = net_salary - ecost
            print("Total saving for {} month is {}:".format((i + 1), total_saving))
            total_saving_list.append(total_saving)



    savings = sum(total_saving_list)

    if savings > 0:
        print('You win')
        print('Consolidate savings {}:'.format(savings))
    else:
        print('You lose')
        print('Consolidate savings {}:'.format(savings))

    cont = input("Do you want to continue,then enter only y or n  Y/N:").lower()
    if cont == 'y':
        flag = True
    else:
        flag = False







