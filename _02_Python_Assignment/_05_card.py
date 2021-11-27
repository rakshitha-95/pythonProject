import itertools
import random
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
types=['heart','spades','diamond','club']
deck=[Card(value,color)for value in range(1,14) for color in types]
values=['A','K','Q','J','1','2','3','4','5','6','7','8','9','10']
cards=list(itertools.product(types,values))
random.shuffle(cards)
for values,types in cards:
    print('the %s of %s' %(values,types))
def player1(n):
    for i in range(n):
        print("player1 :",cards[i][0] , cards[i][1])



def player2(n):
    for j in range(n):
        print("player2 :",cards[j][0] , cards[j][1])

player1(26)
player2(26)