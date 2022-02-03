import random as r

def give_int(str):
    if str == 'rock':
        return 1
    elif str == 'paper':
        return 2
    else:
        return 3

won = 0
x = 5
while(x != 0):
    a = r.randint(1,3)
    print(a)
    b = input("Enter The Element(Rock,Paper,Scissor): \n").lower()
    i = give_int(b)
    if (a == 1 and i == 2) or (a == 2 and i == 3) or ( a == 3 and i == 1):
        print("You Won!!! Congo\n")
        won += 1 
    elif a == i:
        print('Tie')
        x += 1
    else:
        print("You Loose!")
    x -= 1

if won > 3:
    print('Youy Won!! Whole game')
else:
    print("Sorry You loose!")
