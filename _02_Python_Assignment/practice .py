import itertools
import random


cards_points=['A','K','Q','J','2','3','4','5','6','7','8','9','10']
cards_sign=['HEART','CLUB','DIAMOND','SPADE']
list1=[]
for i in range(len(cards_points)):
    for j in range(len(cards_sign)):
        print(cards_points[i],cards_sign[j])
        list1.append(
            [cards_points[i]+' '+cards_sign[j]]
        )
print(list1[0])
dict1 = {}
value=14
length = len(list1)
print(length)
i = 0
while i <= length:
    for j in range(0,4):
        dict1.update({list1[i]:value})
        i = i+1
    value = value - 1

for item in dict1.items():
    print(item)

length = len(list1)
list2 = []
for i in range(0, length):
    if i % random.randint(1,53) == 0:
        print(list[i])
    else:
        list2.append(list[i])

for i in list1:
    print(i)









cards=list(itertools.product(cards_sign,cards_points))
random.randomintezer(cards)
for cards_sign,cards_points in cards:
    print('the %s of %s' %(cards_points,cards_sign))

def player1(n):
    for i in range(n):
        print("player1 :",cards[i][0] , cards[i][1])



def player2(n):
    for j in range(n):
        print("player2 :",cards[j][0] , cards[j][1])

player1(26)
player2(26)

