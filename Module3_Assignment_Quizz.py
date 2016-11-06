#Interactive Quizz program

import random

__author__='Sharath'
__version__='V1.0'

def getRandomNumber(level):
    if level=='easy':
        return random.randint(0,20),random.randint(0,20)
    elif level =='intermediate':
        return random.randint(20,100),random.randint(20,100)
    elif level == 'hard':
        return random.randint(100,1000),random.randint(100,1000)

def displayQuestion(a,b,operation,opdict):
    q='Whats '+str(a)+' '+str(opdict[operation])+'  '+str(b)
    return input(q)

def check(userresponse,a,b,op):
    if op =='M':
        return userresponse==a*b
    elif op=='D':
        return userresponse==a/b
    elif op=='A':
        return userresponse==a+b
    elif op=='S':
        return userresponse==a-b

def displayPositive():
    positives=['Right Answer !','Well Done!','You are a Gem!','You are a machine!']
    print positives[random.randint(0,3)]


def displayNegative():
    positives=['Oops !','You are close !','Check question arefully !','You need a trainer !']
    print positives[random.randint(0,3)]

def main():
    game =True

    while game:

        level=raw_input('Choose a level easy,intermediate,hard')
        level.lower()
        if level not in ('easy','intermediate','hard'):
            print level,' is not a correct level, please choose right one'
            continue

        c=True

        while(c):
            try:
                nofquestions = input('Enter the number of question you need to play')
                if not isinstance(nofquestions,int):
                    raise TypeError
                c=False
            except TypeError:
                print 'Please enter a valid integer try again'

        c=True

        while(c):
            qtype = raw_input('Enter the type of questions (A Addition, S Substraction, M Multiplication, D Division)')
            if qtype not in ('M','S','D','A'):
                print 'Please make a valid selection (M,A,S,D)'
                continue
            c=False

        opdict ={'M':'Multiplied By','S':'Substracted By','A':'Added By','D':'Divide By'}
        pos=0
        neg=0
        i = nofquestions
        while i>0:

            a,b = getRandomNumber(level)
            useranswer= displayQuestion(a,b,qtype.upper(),opdict)
            decision = check(useranswer,a,b,qtype)
            if decision:
                pos+=1
                displayPositive()
            else:
                neg+=1
                displayNegative()
            i-=1

        print 'Total %d Questions played, %d Right Answers %d Wrong Answers'%(nofquestions,pos,neg)

        nextiter = raw_input('Continue or Exit (Continue:C,Exit:E)')
        if nextiter!='C':
            game =False


if __name__=='__main__':
    main()




