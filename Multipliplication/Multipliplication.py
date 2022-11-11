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

def RecMult(a,b):
    if len(a) == 1:
        ml = a[0]*b[0]
        answ = [ml%10]
        if int(math.floor(ml/10)) != 0:
            answ.insert(0,int(math.floor(ml/10)))
        return answ
    if len(a) % 2 == 1:
        a.insert(0)
        b.insert(0)
    halfLen = int(len(a)/2)
    mult1 = RecMult(a[:halfLen], b[:halfLen])
    mult2 = RecMult(a[:halfLen], b[halfLen:])
    mult3 = RecMult(a[halfLen:], b[:halfLen])
    mult4 = RecMult(a[halfLen:], b[halfLen:])
    answ = mult1+SumListNum(mult2,mult3)+mult4
    return answ

def RecMultFast(a,b,n):
    if n == 1:
        return a & b
    if n % 2 == 1: n+=1
    mask = ~(((~0)>>n)<<n)
    halfLen = int(n/2)
    a1 = a >> halfLen
    a2 = ((a << halfLen) & mask)>>halfLen
    b1 = b >> halfLen
    b2 = ((b << halfLen) & mask)>>halfLen
    mult1 = RecMultFast(a1,b1,halfLen)
    mult4 = RecMultFast(a2,b2,halfLen)
    dopmult = 0
    sumA = a1 + a2
    sumB = b1 + b2
    maxN = 1
    if sumA != 0 or sumB != 0:
        maxN = max(math.ceil(math.log2(sumA+0.1)), math.ceil(math.log2(sumB+0.1)))
    dopmult = RecMultFast(sumA,sumB,maxN)
    return (mult1<<n) + ((dopmult - mult1 - mult4)<<halfLen) + mult4

def mult(a, b, isFast = False):
    #if (a == 0) or (b == 0): return 0
    digitCount = max(len(a), len(b))
    for i in range(digitCount - len(a)):
        b.insert(0,0)
    for i in range(digitCount - len(b)):
        a.insert(0,0)
    #if digitCount % 2 == 1: digitCount+=1
    if isFast:
        return RecMultFast(a, b, digitCount)
    else:
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
print(ColumnMult(num1, num2))
print("N1: ",N1)