inp = input()
inpArr = []
nums = [0,1,2,3,4,5,6,7,8,9,"0","1","2","3","4","5","6","7","8","9"]

# -2*(-4--3)

# добавляю пробелы
for i in range(len(inp)):
    if inp[i] == "*" and inp[i-1] != " " and inp[i+1]:
        inpArr.append(" * ")
    elif inp[i] == "/" and inp[i-1] != " " and inp[i+1]:
        inpArr.append(" / ")
    elif inp[i] == "+" and inp[i-1] != " " and inp[i+1]:
        inpArr.append(" + ")
    elif inp[i] == "-" and inp[i-1] in nums and inp[i-1] != " " and inp[i+1]:
        inpArr.append(" - ")
    else:
        inpArr.append(inp[i])
inp = ""
for i in inpArr:
    inp += i

# преобр в инт
def _int(e):
    return ord(e)-48

# пропуск пробелов
def canselSpace(a):
    while " " in a:
        a = a.replace(" ", "")
    return a

def _calc(vyr):
    if "*" in vyr:
        vyr = canselSpace(vyr)
        vyr = list(vyr.split("*"))
        num1 = []
        n1 = vyr[0]
        otr1 = False
        if "." in n1:
            a1 = n1.split(".")
            z1 = a1[0]
            dr1 = a1[1]
            zInt1 = []
            drInt1 = []
            drLen1 = 10 ** len(a1[1])
            for i in z1:
                if i == "-":
                    otr1 = True
                else:
                    zInt1.append(_int(i))
            for i in dr1:
                drInt1.append(_int(i))
            zN1 = 0
            drN1 = 0
            for i in zInt1:
                zN1 *= 10
                zN1 += i
            for i in drInt1:
                drN1 *= 10
                drN1 += i
            num1.append(zN1 + drN1 / drLen1)
        else:
            for i in n1:
                if i == "-":
                    otr1 = True
                else:
                    num1.append(_int(i))
        num2 = []
        n2 = vyr[1]
        otr2 = False
        if "." in n2:
            a2 = n2.split(".")
            z2 = a2[0]
            dr2 = a2[1]
            zInt2 = []
            drInt2 = []
            drLen2 = 10 ** len(a2[1])
            for i in z2:
                if i == "-":
                    otr2 = True
                else:
                    zInt2.append(_int(i))
            for i in dr2:
                drInt2.append(_int(i))
            zN2 = 0
            drN2 = 0
            for i in zInt2:
                zN2 *= 10
                zN2 += i
            for i in drInt2:
                drN2 *= 10
                drN2 += i
            num2.append(zN2 + drN2 / drLen2)
        else:
            for i in n2:
                if i == "-":
                    otr2 = True
                else:
                    num2.append(_int(i))
        numm1 = 0
        numm2 = 0
        for i in num1:
            numm1 *= 10
            numm1 += i
        for i in num2:
            numm2 *= 10
            numm2 += i
        if otr1 == True:
            numm1 *= -1
        if otr2 == True:
            numm2 *= -1

        return (numm1 * numm2)

    if "/" in vyr:
        vyr = canselSpace(vyr)
        vyr = list(vyr.split("/"))
        num1 = []
        n1 = vyr[0]
        otr1 = False
        if "." in n1:
            a1 = n1.split(".")
            z1 = a1[0]
            dr1 = a1[1]
            zInt1 = []
            drInt1 = []
            drLen1 = 10 ** len(a1[1])
            for i in z1:
                if i == "-":
                    otr1 = True
                else:
                    zInt1.append(_int(i))
            for i in dr1:
                drInt1.append(_int(i))
            zN1 = 0
            drN1 = 0
            for i in zInt1:
                zN1 *= 10
                zN1 += i
            for i in drInt1:
                drN1 *= 10
                drN1 += i
            num1.append(zN1 + drN1 / drLen1)
        else:
            for i in n1:
                if i == "-":
                    otr1 = True
                else:
                    num1.append(_int(i))
        num2 = []
        n2 = vyr[1]
        otr2 = False
        if "." in n2:
            a2 = n2.split(".")
            z2 = a2[0]
            dr2 = a2[1]
            zInt2 = []
            drInt2 = []
            drLen2 = 10 ** len(a2[1])
            for i in z2:
                if i == "-":
                    otr2 = True
                else:
                    zInt2.append(_int(i))
            for i in dr2:
                drInt2.append(_int(i))
            zN2 = 0
            drN2 = 0
            for i in zInt2:
                zN2 *= 10
                zN2 += i
            for i in drInt2:
                drN2 *= 10
                drN2 += i
            num2.append(zN2 + drN2 / drLen2)
        else:
            for i in n2:
                if i == "-":
                    otr2 = True
                else:
                    num2.append(_int(i))
        numm1 = 0
        numm2 = 0
        for i in num1:
            numm1 *= 10
            numm1 += i
        for i in num2:
            numm2 *= 10
            numm2 += i
        if otr1 == True:
            numm1 *= -1
        if otr2 == True:
            numm2 *= -1
        return (numm1 / numm2)

    if "+" in vyr:
        vyr = canselSpace(vyr)
        vyr = list(vyr.split("+"))
        num1 = []
        n1 = vyr[0]
        otr1 = False
        if "." in n1:
            a1 = n1.split(".")
            z1 = a1[0]
            dr1 = a1[1]
            zInt1 = []
            drInt1 = []
            drLen1 = 10 ** len(a1[1])
            for i in z1:
                if i == "-":
                    otr1 = True
                else:
                    zInt1.append(_int(i))
            for i in dr1:
                drInt1.append(_int(i))
            zN1 = 0
            drN1 = 0
            for i in zInt1:
                zN1 *= 10
                zN1 += i
            for i in drInt1:
                drN1 *= 10
                drN1 += i
            num1.append(zN1 + drN1 / drLen1)
        else:
            for i in n1:
                if i == "-":
                    otr1 = True
                else:
                    num1.append(_int(i))
        num2 = []
        n2 = vyr[1]
        otr2 = False
        if "." in n2:
            a2 = n2.split(".")
            z2 = a2[0]
            dr2 = a2[1]
            zInt2 = []
            drInt2 = []
            drLen2 = 10 ** len(a2[1])
            for i in z2:
                if i == "-":
                    otr2 = True
                else:
                    zInt2.append(_int(i))
            for i in dr2:
                drInt2.append(_int(i))
            zN2 = 0
            drN2 = 0
            for i in zInt2:
                zN2 *= 10
                zN2 += i
            for i in drInt2:
                drN2 *= 10
                drN2 += i
            num2.append(zN2 + drN2 / drLen2)
        else:
            for i in n2:
                if i == "-":
                    otr2 = True
                else:
                    num2.append(_int(i))
        numm1 = 0
        numm2 = 0
        for i in num1:
            numm1 *= 10
            numm1 += i
        for i in num2:
            numm2 *= 10
            numm2 += i
        if otr1 == True:
            numm1 *= -1
        if otr2 == True:
            numm2 *= -1
        return (numm1 + numm2)

    if "-" in vyr:
        vyr = canselSpace(vyr)
        vyr = list(vyr.split("-",1))
        num1 = []
        n1 = vyr[0]
        otr1 = False
        if "." in n1:
            a1 = n1.split(".")
            z1 = a1[0]
            dr1 = a1[1]
            zInt1 = []
            drInt1 = []
            drLen1 = 10 ** len(a1[1])
            for i in z1:
                if i == "-":
                    otr1 = True
                else:
                    zInt1.append(_int(i))
            for i in dr1:
                drInt1.append(_int(i))
            zN1 = 0
            drN1 = 0
            for i in zInt1:
                zN1 *= 10
                zN1 += i
            for i in drInt1:
                drN1 *= 10
                drN1 += i
            num1.append(zN1+drN1/drLen1)
        else:
            for i in n1:
                if i == "-":
                    otr1 = True
                else:
                    num1.append(_int(i))
        num2 = []
        n2 = vyr[1]
        otr2 = False
        if "." in n2:
            a2 = n2.split(".")
            z2 = a2[0]
            dr2 = a2[1]
            zInt2 = []
            drInt2 = []
            drLen2 = 10 ** len(a2[1])
            for i in z2:
                if i == "-":
                    otr2 = True
                else:
                    zInt2.append(_int(i))
            for i in dr2:
                drInt2.append(_int(i))
            zN2 = 0
            drN2 = 0
            for i in zInt2:
                zN2 *= 10
                zN2 += i
            for i in drInt2:
                drN2 *= 10
                drN2 += i
            num2.append(zN2+drN2/drLen2)
        else:
            for i in n2:
                if i == "-":
                    otr2 = True
                else:
                    num2.append(_int(i))
        numm1 = 0
        numm2 = 0
        for i in num1:
            numm1 *= 10
            numm1 += i
        for i in num2:
            numm2 *= 10
            numm2 += i
        if otr1 == True:
            numm1 *= -1
        if otr2 == True:
            numm2 *= -1
        return (numm1 - numm2)

while "(" in inp:
    s1 = inp.index("(")
    s2 = inp.index(")") + 1
    _take = inp[s1:s2]
    _toCalc = _take.replace("(", "")
    _toCalc = _toCalc.replace(")", "")
    calceed = _calc(_toCalc)
    inp = inp.replace(_take, str(calceed))

inp = inp.split(" ")
inp = list(inp)

# сначала делаем умножение и деление
while "*" in inp or "/" in inp:
    if "*" in inp:
        ind = inp.index("*")
        x = inp[ind - 1]
        oper = inp[ind]
        y = inp[ind + 1]
        inp.pop(ind)
        inp.pop(ind)
        toCalc = x + oper + y
        res = _calc(toCalc)
        inp[ind - 1] = str(res)

    if "/" in inp:
        ind = inp.index("/")
        x = inp[ind - 1]
        oper = inp[ind]
        y = inp[ind + 1]
        inp.pop(ind)
        inp.pop(ind)
        toCalc = x + oper + y
        res = _calc(toCalc)
        inp[ind - 1] = str(res)

# потом делаем сложение и вычитание
while "+" in inp or "-" in inp:
    if "+" in inp:
        ind = inp.index("+")
        x = inp[ind-1]
        oper = inp[ind]
        y = inp[ind+1]
        inp.pop(ind)
        inp.pop(ind)
        toCalc = x + oper + y
        res = _calc(toCalc)
        inp[ind - 1] = str(res)

    if "-" in inp:
        ind = inp.index("-")
        x = inp[ind - 1]
        oper = inp[ind]
        y = inp[ind + 1]
        inp.pop(ind)
        inp.pop(ind)
        toCalc = x + oper + y
        res = _calc(toCalc)
        inp[ind - 1] = str(res)

print(inp[0])
