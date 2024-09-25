def op(ins):
    if ins == "LOAD":
        return "00000001"
    elif ins == "STOR":
        return "00100001"
    elif ins == "DIV":
        return "00001100"
    elif ins == "ADD":
        return "00000101"
    elif ins == "JUMP":
        return "00001101"
    elif ins == "POWER":
        return "00100011"
    elif ins == "LEN":
        return "01100011"
    elif ins == "LOAD MQ,M(0)":
        return "00001001"
    elif ins == "LOAD MQ":
        return "00001010"
    else:
        return "0"

def binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        if n % 2 == 0:
            return binary(n // 2) + "0"
        else:
            return binary(n // 2) + "1"

def add0(a):
    n = 12 - len(a)
    return '0' * n + a

def Input(m):
    print("Assembly Program: ")
    while True:
        a = input()
        if a == "HALT":
            break
        else:
            y = ""
            strbin = ""

            if "JUMP" in a:
                y = op("JUMP")
                strbin = binary(int(a[7]))
                strbin = add0(strbin)
                y += strbin
                y = "0"*20 + y
            elif "STOR" in a:
                y = op("STOR")
                strbin = binary(int(a[7]))
                strbin = add0(strbin)
                y += strbin
                if "LOAD" in a:
                    y += op("LOAD MQ,M(0)")
                    strbin = binary(int(a[20]))
                    strbin = add0(strbin)
                    y += strbin
                else:
                    y = "0"*20 + y
            elif "LEN" in a:
                y = op("LOAD")
                strbin = binary(int(a[7]))
                strbin = add0(strbin)
                y += strbin
                y += op("LEN")
                y += "0"*12

            elif "LOAD MQ" in a:
                y = op("LOAD MQ")
                y += "0"*12
                y += op("DIV")
                strbin = binary(int(a[14]))
                strbin = add0(strbin)
                y += strbin
 
            elif "POWER" in a:
                y = op("POWER")
                strbin = binary(int(a[9]))
                strbin = add0(strbin)
                y += strbin
                y += op("ADD")
                strbin = binary(int(a[19]))
                strbin = add0(strbin)
                y += strbin

            m.append(y)
    print("Binary :")
    for j in m:
        print(j)

