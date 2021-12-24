#HANDCRICKET GAME IN PYTHON ( 1 VS 1 )                                  #SUBMITTED BY:
                                                                        #Name of the student: ANIRUDH PARASARAN R
                                                                        #Registration Number: 21BRS1471
import random #importing random module to the program namespace
print()
toss=input('Enter H or T: ') #H for team A and T for Team B (only uppercase H or T allowed)
if toss=='H':
    print('TEAM A WON THE TOSS AND CHOOSE TO BAT FIRST')
    print()
else:
    print('TEAM B WON THE TOSS AND CHOOSE TO BOWL FIRST')
    print()
#The team that loses the toss will have to bowl first
n=int(input('Enter the number of balls you wish to play: ')) #The number of balls for the match
print()
x=[]
for i in range(n):
    a=int(input('Enter a number between 1 to 6: '))
    print()
    if a>=1 and a<=6:
        b=random.randint(1,6) #randint is usd to generate numbers within the specified range (upperlimit is included)
        if a==b:
            print('WICKET, NO MORE WICKETS REMAINING')
            break
        else:
            x.append(a)
            continue
    else:
        print('Invalid input')
        break
print('Total runs scored by team A: ', sum(x)) #total runs scored by team A
print()
print('Target for Team B: ', sum(x)+1) #target is always 1 run more than the score
print()
y=[]
for i in range(n):
        c=int(input('Enter a number between 1 to 6: '))
        print()
        if c>=1 and c<=6:
            d=random.randint(1,6)
            if c==d:
                print('WICKET, NO MORE WICKETS REMAINING')
                break
            else:
                y.append(c)
                if sum(x)<sum(y):
                    break
                else:
                    continue
        else:
            print('Invalid input')
            break
print('Total runs scored by team B: ',sum(y))
print()
if sum(y)>=sum(x)+1:
    print()
    print('TEAM B WON THE MATCH')
elif sum(y)==sum(x):
    print()
    print('MATCH TIED')
else:
    print()
    print('TEAM A WON THE MATCH')
    

