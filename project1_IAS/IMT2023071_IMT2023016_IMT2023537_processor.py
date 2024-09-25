from IMT2023071_IMT2023016_IMT2023537_assembler import *

MAR, IR, PC, IBR = "", "", 0, ""
AC, MQ, MBR, M = 0, 1, 0, [1, 10, 0, 0]
memory = []
def processor(op, addr):
    global AC, MQ, MBR
    addr= "0b"+addr
    if op == "00000001":#load
        MBR = M[int(addr, 2)]
        AC = MBR
        print("load-----------------------")
        print("AC: ", AC)

    elif op == "00100001":#stor
        MBR = AC
        M[int(addr, 2)] = MBR
        print("stor-----------------------")
        print("AC: ", AC)
    elif op == "00000101":#add
        MBR = M[int(addr, 2)]
        AC = AC + MBR
        print("add-----------------------")
        print("AC: ", AC)
    elif op == "00001100":#div
        MBR = M[int(addr, 2)]
        MQ = AC // MBR
        AC = AC % MBR
        print("div-----------------------")
        print("AC: ", AC)
        print("MQ: ", MQ)
    elif op == "00001001":#load mq m(0)
        MQ=M[int(addr, 2)]
        print("load mq m(0)-----------------------")
        print("MQ: ",MQ)
    elif op == "00001010":#Load mq
        AC = MQ
        print("load mq-----------------------")     
        print("AC: ", AC)

    elif op == "00100011":#power
        MBR = M[int(addr, 2)]
        AC = AC**MBR
        print("power-----------------------")
        print("AC: ", AC)

    elif op == "01100011":#Len
        AC=len(str(AC))
        print("len-----------------------")
        print("AC: ", AC)

    elif op == "00001101":#jump
        print("jump-----------------------")
        PC = int(addr,2)
        print("PC: ",PC)

def decoder(inst):
    global MAR, IR, PC, IBR
    LHS, RHS, Lop, Rop, Laddr, Raddr = "", "", "", "", "", ""
    MAR = PC
    
    LHS = inst[0:20]
    Lop = LHS[0:8]
    Laddr = LHS[8:20]

    RHS = inst[20:40]
    Rop = RHS[0:8]
    Raddr = RHS[8:20]
    MAR,IBR,IR =Laddr,RHS,Lop
    processor(Lop, Laddr)
    PC+=1

    MAR, IR = Raddr, Rop
    processor(Rop, Raddr)


Input(memory)
n = int(input("Enter a number: "))
M[0] = n

decoder(memory[0])
decoder(memory[1])

N = 2
count=0
while count<len(str(n)) :
    decoder(memory[N])
    if "00001101" in memory[N]:
            N = 2
            count+=1
    else:
        N += 1
print("Final result (1: if Armstrong number, 0: if not)")
if M[3]==M[0]:
    print(1)
else:
    print(0)
