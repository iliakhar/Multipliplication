
import math

N1 = 0

def SumListNum(a, b):
    #global N1
    for i in range(0, len(a)-len(b), 1):
        b.insert(0,0)
    for i in range(0, len(b)-len(a), 1):
        a.insert(0,0)
    answ = []
    numSum = digit = 0
    for i in range(len(a)-1, -1, -1):
        #N1 += 1
        numSum = a[i] + b[i] + digit
        digit = int(math.floor(numSum/10))
        answ.insert(0,numSum % 10)
    if digit != 0:
        answ.insert(0,digit)
    return answ

def DifListNum(a, b):
    #global N1

    answ = []
    numDif = 0
    for i in range(len(b)):
        #N1 += 1
        numDif = a[len(a) - i - 1] - b[len(b) - i - 1]
        if(numDif<0):
            numDif+=10
            a[len(a) - i - 2]-=1
        answ.insert(0,numDif)

    answ = a[:-len(b)] + answ
    while(len(answ)>0 and answ[0] == 0):
        answ.pop(0)
    return answ

def SpecialSum(a, b):
    global N1
    if len(a)>len(b): b.insert(0,0)
    elif len(b)>len(a): a.insert(0,0)
    fl = [a[0]*b[0]]
    fl.extend([0]*2*(len(a)-1))
    summ = []
    if(a[0] == 0 or b[0] == 0):
        if a[0] == 0: summ = a[1:]
        else: summ = b[1:]
    else: 
        #N1 += 1
        summ = SumListNum(b[1:], a[1:])
    summ.extend([0]*(len(a)-1))
    ab = RecMult(b[1:], a[1:])
    answ=[]
    if(fl[0]!=0):
        answ = SumListNum(fl, summ)
        answ = SumListNum(answ, ab)
    else: answ = answ = SumListNum(summ, ab)
    return answ

def RecMult(a,b):
    global N1
    if len(a) == 1:
        N1 += 1
        ml = a[0]*b[0]
        answ = [ml%10]
        if int(math.floor(ml/10)) != 0:
            answ.insert(0,int(math.floor(ml/10)))
        return answ

    halfLen = int(math.ceil(len(a)/2))
    #N1+=1
    v = RecMult(a[:-halfLen], b[:-halfLen])
    w = RecMult(a[-halfLen:], b[-halfLen:])
    sumAB = SumListNum(a[:-halfLen],a[-halfLen:])
    sumCD = SumListNum(b[:-halfLen],b[-halfLen:])
    if(len(sumAB)>halfLen or len(sumCD)>halfLen):
         u = SpecialSum(sumAB,sumCD)
    else: u = RecMult(sumAB, sumCD)
    
    #u = RecMult(sumAB, sumCD)
    
    #N1+=2
    u = DifListNum(u,v)
    u = DifListNum(u,w)
    u.extend([0]*halfLen)
    v.extend([0]*2*halfLen)
    answ = SumListNum(u,v)
    answ = SumListNum(answ,w)
    return answ


def mult(a, b, isFast = False):
    digitCount = max(len(a), len(b))
    for i in range(digitCount - len(a)):
        b.insert(0,0)
    for i in range(digitCount - len(b)):
        a.insert(0,0)

    return RecMult(a, b)


def ColumnMult(a, b):
    answ = []
    global N1
    N1 = countWrToAnsw = 0
    for i in range(len(b)):
        remB = b[len(b)-1-i]
        digit = 0
        miniAnsw = [0]*i
        if remB != 0:
            for j in range(len(a)):
                
                remA = a[len(a)-1-j]
                if remA != 0 or digit != 0:
                    N1+=2
                    multNum = remA * remB + digit
                    digit = math.floor(multNum / 10)
                    miniAnsw.insert(0,math.floor(multNum % 10))
                else: miniAnsw.insert(0,0)
            if digit != 0: miniAnsw.insert(0, digit)
            if countWrToAnsw != 0:
                answ = SumListNum(answ, miniAnsw)
                N1 += 1
            else: answ = miniAnsw
            countWrToAnsw += 1
    return answ

def StrToList(s):
    lst = []
    for i in s:
        lst.append(ord(i) - ord('0'))
    return lst

def GetNumbers():
    print("Enter First Num: ", end = "");
    a = input()
    print("\nEnter Second Num: ", end = "");
    b = input()
    print()
    a1 = StrToList(a)
    return a1,StrToList(b)

#print(mult([9,8], [9,8]))
#print(mult(43, 2512, True))
num1, num2 = GetNumbers()
print(mult(num1, num2))
#print(mult([2,3,4,5], [7,9,8,6]))
print("N1: ",N1)
#print(RecMult([9,9,9],[9,9,9]))