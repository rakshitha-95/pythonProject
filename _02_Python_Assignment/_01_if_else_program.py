sub1=float(input("enter the 1 st lang marks"))
sub2=float(input("enter the 2 nd lang marks"))
sub3=float(input("enter the 3 rd lang marks "))
sub4=float(input("enter the mathematics marks"))
sub5=float(input("enter the science marks"))
sub6=float(input("enter the social marks"))
total=((sub1+sub2+sub3+sub4+sub5+sub6)/600)*100
list1=[sub1,sub2,sub3,sub4,sub5,sub6]
list1.sort()
summation = list1[3]+list1[4]+list1[5]
avg = ((summation/300)*100)

if total>=90:
    print("distinction")
    if avg>=95:
        print("goldmedal")
elif 75 < total <90:
    print("average")
else:
    print("fail")















