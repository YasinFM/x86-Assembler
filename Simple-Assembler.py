
'''
Author: MohammadYasin Farshad
Des 2023
This progtam is a simple assembeller which can support the following instructions:
        ADD, SUB, AND, OR, INC, DEC, XOR, PUSH, POP and JMP

<<< This program does not support octal numbers >>>
'''

###   Start Of Definding Registers   ###

eax = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ebx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ecx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
edx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
esp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
esi = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
edi = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ebp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

ax = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
si = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
di = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

al = [0,0,0,0,0,0,0,0]
ah = [0,0,0,0,0,0,0,0]
bl = [0,0,0,0,0,0,0,0]
bh = [0,0,0,0,0,0,0,0]
cl = [0,0,0,0,0,0,0,0]
ch = [0,0,0,0,0,0,0,0]
dl = [0,0,0,0,0,0,0,0]
dh = [0,0,0,0,0,0,0,0]

stack = []

all_registers = {"eax": eax ,"ebx": ebx ,"ecx": ecx ,"edx": edx ,"esp": esp ,"esi": esi ,"edi": edi ,"ebp": ebp ,
                 "ax": ax ,"bx": bx ,"cx": cx ,"dx": dx ,"sp": sp ,"si": si ,"di": di ,"bp": bp,
                  "al": al ,"ah": ah ,"bl": bl ,"bh": bh ,"cl": cl ,"ch": ch ,"dl": dl ,"dh": dh}

###   End Of Definding Registers   ###

###   Start Of OpCode Definitions   ###

reg32Bit = {
  "eax" :"000", "ebx" :"011", "ecx" :"001", "edx" :"010",
  "esp" :"100", "esi" :"110", "edi" :"111", "ebp" :"101"
}

reg16Bit = {
  "ax" :"000", "bx" :"011", "cx" :"001", "dx" :"010",
  "sp" :"100", "si" :"110", "di" :"111", "bp" :"101"
}
reg8Bit = {
  "al" :"000", "bl" :"011", "cl" :"001", "dl" :"010",
  "ah" :"100", "bh" :"111", "ch" :"101", "dh" :"110"
}
opCodesInstruction = {
    "add" :"000000", "sub" :"001010", "inc" :"111111", "dec" :"111111",
    "or"  :"000010", "and" :"001000", "xor" :"001100"
}

###   End Of OpCode Definitions   ###

###   Start Of Definding Needed Functions   ###

def binary_to_decimal(register):
    decimal = 0
    power = len(register) - 1
    for i in range(0,len(register)):
        decimal += (register[i] * (2 ** power))
        power -= 1
    return decimal

def decimal_to_binary(decimal,register):
    counter = len(register)
    for i in range(counter - 1,-1,-1):
        register[i] = decimal % 2
        decimal //= 2
    return None

def hexa_to_decimal(hexadecimal):
    decimal = 0
    power = 0
    while hexadecimal != "":
        l = len(hexadecimal) - 1
        if "0" <= hexadecimal[l] <= "9":
            decimal += (int(hexadecimal[l]) * (16 ** power))
        elif 97 <= ord(hexadecimal[l]) <= 102:
            value = ord(hexadecimal[l]) - 87
            decimal += (value * (16 ** power))
        elif 65 <= ord(hexadecimal[l]) <= 70:
            value = ord(hexadecimal[l]) - 55
            decimal += (value * (16 ** power))
        else:
            return -1
        hexadecimal = hexadecimal[0:l]
        power += 1
    return decimal

def decimal_to_bin(decimal):
    binary = ""
    if decimal == 0 :
        return str(decimal)
    while decimal != 0 :
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def string_to_decimal(string):
    string = str(string)
    if string[len(string) - 1] == 'h':
        string = string[:len(string) - 1]
        decimal = hexa_to_decimal(string)
    elif string[len(string) - 1] == 'b' or string[len(string) - 1] == 'y':
        string = string[:len(string) - 1]
        decimal = binary_to_decimal(string)
    else:
        if string[len(string) - 1] == 'd' or string[len(string) - 1] == 't':
            string = string[:len(string) - 1]
        decimal = int(string)
    return decimal

def add(register,string):
    decimal = string_to_decimal(string)
    decimalreg = binary_to_decimal(register)
    decimal_to_binary(decimal + decimalreg , register)
    return None

def sub(register,string):
    decimal = string_to_decimal(string)
    decimalreg = decimal_to_binary(register)
    binary_to_decimal(decimal - decimalreg , register)
    return None

def add_register(register1,register2):
    if len(register1) != len(register2):
        return -1
    decimal1 = binary_to_decimal(register1)
    decimal2 = binary_to_decimal(register2)
    decimal_to_binary(decimal1 + decimal2 , register1)
    return None

def sub_register(register1,register2):
    if len(register1) != len(register2):
        return -1
    decimal1 = binary_to_decimal(register1)
    decimal2 = binary_to_decimal(register2)
    decimal_to_binary(decimal1 - decimal2 , register1)
    return None

def inc(register):
    return add(register,1)

def dec(register):
    return sub(register,1)

def and_imm(register,string):
    decimal = string_to_decimal(string)
    binary = decimal_to_bin(decimal)
    if len(binary) < len(register):
        binary = ("0" * len(register) - len(binary)) + binary
    for i in range(len(register) - 1 , -1 , -1):
        if register[i] == 1 and binary[i] == 1:
            register[i] = 1
        else:
            register[i] = 0
    return None

def or_imm(register,string):
    decimal = string_to_decimal(string)
    binary = decimal_to_bin(decimal)
    if len(binary) < len(register):
        binary = ("0" * len(register) - len(binary)) + binary
    for i in range(len(register) - 1 , -1 , -1):
        if register[i] == 1 or binary[i] == 1:
            register[i] = 1
        else:
            register[i] = 0
    return None

def and_reg(register1,register2):
    if len(register1) != len(register2):
        return -1
    for i in range(len(register1)):
        if register1[i] == 1 and register2[i] == 1:
            register1[i] = 1
        else:
            register1[i] = 0
    return None

def or_reg(register1,register2):
    if len(register1) != len(register2):
        return -1
    for i in range(len(register1)):
        if register1[i] == 1 or register2[i] == 1:
            register1[i] = 1
        else:
            register1[i] = 0
    return None

def xor_imm(register,string):
    decimal = string_to_decimal(string)
    binary = decimal_to_bin(decimal)
    if len(binary) < len(register):
        binary = ("0" * len(register) - len(binary)) + binary
    for i in range(len(register) - 1 , -1 , -1):
        if register[i] == binary[i]:
            register[i] = 0
        else:
            register[i] = 1
    return None

def xor_reg(register1,register2):
    if len(register1) != len(register2):
        return -1
    for i in range(len(register1)):
        if register1[i] == register2[i]:
            register1[i] = 0
        else:
            register1[i] = 1
    return None

'''
def push_imm():

def push_reg():

def pop():

def jmp():

'''
def opcode_reg_to_reg(register1,register2):
    extra_bit = ''
    if asm_line[1] in reg8Bit:
        s = '0'
        r_m = reg8Bit[register2]
        reg = reg8Bit[register1]
    else:
        s = '1'
        if asm_line[1] in reg16Bit:
            r_m = reg16Bit[register2]
            reg = reg16Bit[register1]
            extra_bit = "66 "
        else:
            reg = reg32Bit[register2]
            r_m = reg32Bit[register1]
    return extra_bit,s,r_m,reg

###   End Of Definding Needed Functions   ###

###   Start Of Processing   ###

## Getting Inputs ##

while True:
    print("Select which way you wish to enter the assembely code:")
    print("1. With File")
    print("2. Entring code using terminal")
    entering_code = input()
    if entering_code != '1' and entering_code != '2':
        print("Error!!!\nTry agian!")
        continue
    else:
        break

asm_code = []
if entering_code == '1':
    file_address = input("Enter the file address:")
    asmfile = open(file_address)
    for each_line in asmfile:
        asm_code += [each_line]

else:
    print("Enter the codes:")
    while True:
        each_line = input()
        if each_line == '':
            break
        asm_code += [each_line]

## Compiling The Inputs 

label = {}
for i in range(len(asm_code)):
    string = asm_code[i].split(":")
    string_instruction = string[len(string)-1].split()[0].lower()
    string_reg = string[len(string)-1].split()[1].split(",")
    for j in range(len(string_reg)):
        string_reg[j] = string_reg[j].lower()
    asm_code[i] = [string_instruction , string_reg]

    if len(string) > 1:
        label[string[0].lower()] = i

## Starting to Process The Opcodes
         
address = "0x0000000000000000"
address_list = []

for i in range(len(asm_code)):
    asm_ins = asm_code[i][0]
    asm_line = asm_code[i][1]
    if asm_ins == "add" or asm_ins == "sub" or asm_ins == "and" or asm_ins == "or" or asm_ins == "xor":
        r_memory = asm_line[1][1:len(asm_line[1])-1]
        l_memory = asm_line[0][1:len(asm_line[0])-1]
        if asm_ins == "add":
            if ((asm_line[1] in reg32Bit) and (asm_line[0] in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((asm_line[1] in reg8Bit) and (asm_line[0] in reg8Bit)):
                add_register(all_registers[asm_line[0]],all_registers[asm_line[1]])
                d = '0'
                mod = '11'
                extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],asm_line[1])
            else:
                mod = '00'
                if ((r_memory in reg32Bit) and (asm_line[0] in reg32Bit)) or ((r_memory in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((r_memory in reg8Bit) and (asm_line[0] in reg8Bit)):
                    add_register(all_registers[asm_line[0]],all_registers[r_memory])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],r_memory)
                    d = '1'
                elif ((asm_line[1] in reg32Bit) and (l_memory in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (l_memory in reg16Bit)) or ((asm_line[1] in reg8Bit) and (l_memory in reg8Bit)):
                    add_register(all_registers[l_memory],all_registers[asm_line[1]])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(l_memory,asm_line[1])
                    d = '0'
                else:
                    add(all_registers[asm_line[0]],asm_line[1])
        elif asm_ins == "sub":
            if ((asm_line[1] in reg32Bit) and (asm_line[0] in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((asm_line[1] in reg8Bit) and (asm_line[0] in reg8Bit)):
                sub_register(all_registers[asm_line[0]],all_registers[asm_line[1]])
                extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],asm_line[1])
                d = '0'
                mod = '11'
            else:
                mod = '00'
                if ((r_memory in reg32Bit) and (asm_line[0] in reg32Bit)) or ((r_memory in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((r_memory in reg8Bit) and (asm_line[0] in reg8Bit)):
                    sub_register(all_registers[asm_line[0]],all_registers[r_memory])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],r_memory)
                    d = '1'
                elif ((asm_line[1] in reg32Bit) and (l_memory in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (l_memory in reg16Bit)) or ((asm_line[1] in reg8Bit) and (l_memory in reg8Bit)):
                    sub_register(all_registers[l_memory],all_registers[asm_line[1]])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(l_memory,asm_line[1])
                    d = '0'
                else:
                    sub(all_registers[asm_line[0]],all_registers[asm_line[1]])
        elif asm_ins == "and":
            if ((asm_line[1] in reg32Bit) and (asm_line[0] in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((asm_line[1] in reg8Bit) and (asm_line[0] in reg8Bit)):
                and_reg(all_registers[asm_line[0]],all_registers[asm_line[1]])
                extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],asm_line[1])
                d = '0'
                mod = '11'
            else:
                mod = '00'
                if ((r_memory in reg32Bit) and (asm_line[0] in reg32Bit)) or ((r_memory in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((r_memory in reg8Bit) and (asm_line[0] in reg8Bit)):
                    and_reg(all_registers[asm_line[0]],all_registers[r_memory])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],r_memory)
                    d = '1'
                elif ((asm_line[1] in reg32Bit) and (l_memory in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (l_memory in reg16Bit)) or ((asm_line[1] in reg8Bit) and (l_memory in reg8Bit)):
                    and_reg(all_registers[l_memory],all_registers[asm_line[1]])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(l_memory,asm_line[1])
                    d = '0'
                else:
                    and_imm(all_registers[asm_line[0]],all_registers[asm_line[1]])
        elif asm_ins == "or":
            if ((asm_line[1] in reg32Bit) and (asm_line[0] in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((asm_line[1] in reg8Bit) and (asm_line[0] in reg8Bit)):
                or_reg(all_registers[asm_line[0]],all_registers[asm_line[1]])
                extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],asm_line[1])
                d = '0'
                mod = '11'
            else:
                mod = '00'
                if ((r_memory in reg32Bit) and (asm_line[0] in reg32Bit)) or ((r_memory in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((r_memory in reg8Bit) and (asm_line[0] in reg8Bit)):
                    or_reg(all_registers[asm_line[0]],all_registers[r_memory])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],r_memory)
                    d = '1'
                elif ((asm_line[1] in reg32Bit) and (l_memory in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (l_memory in reg16Bit)) or ((asm_line[1] in reg8Bit) and (l_memory in reg8Bit)):
                    or_reg(all_registers[l_memory],all_registers[asm_line[1]])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(l_memory,asm_line[1])
                    d = '0'
                else:
                    or_imm(all_registers[asm_line[0]],all_registers[asm_line[1]])
        elif asm_ins == "xor":
            if ((asm_line[1] in reg32Bit) and (asm_line[0] in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((asm_line[1] in reg8Bit) and (asm_line[0] in reg8Bit)):
                xor_reg(all_registers[asm_line[0]],all_registers[asm_line[1]])
                extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],asm_line[1])
                d = '0'
                mod = '11'
            else:
                mod = '00'
                if ((r_memory in reg32Bit) and (asm_line[0] in reg32Bit)) or ((r_memory in reg16Bit ) and (asm_line[0] in reg16Bit)) or ((r_memory in reg8Bit) and (asm_line[0] in reg8Bit)):
                    xor_reg(all_registers[asm_line[0]],all_registers[r_memory])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(asm_line[0],r_memory)
                    d = '1'
                elif ((asm_line[1] in reg32Bit) and (l_memory in reg32Bit)) or ((asm_line[1] in reg16Bit ) and (l_memory in reg16Bit)) or ((asm_line[1] in reg8Bit) and (l_memory in reg8Bit)):
                    xor_reg(all_registers[l_memory],all_registers[asm_line[1]])
                    extra_bit, s, r_m, reg = opcode_reg_to_reg(l_memory,asm_line[1])
                    d = '0'
                else:
                    xor_imm(all_registers[asm_line[0]],all_registers[asm_line[1]])

        ### Printing Address
        i = 0
        if ((asm_line[1] in reg16Bit) and (asm_line[0] in reg16Bit)) or ((asm_line[1] in reg16Bit) and (l_memory in reg16Bit)) or ((r_memory in reg16Bit) and (asm_line[0] in reg16Bit)):
            i = 1
        print(address + ":",end = "\t")
        address = int(address,16)
        address_list += [address]
        address = address + 2 + i
        address = hex(address)
        address = address[2:]
        for j in range(16 - len(address)):
            address = '0' + address
        address = "0x" + address

        ### Printing Opcode
        opcode = extra_bit + opCodesInstruction[asm_ins] + d + s + mod + reg + r_m
        opcode = str(hex(int(opcode,2))[2:])
        for j in range(4 - len(opcode)):
            opcode = '0' + opcode
        print(extra_bit + opcode[:2] + " " + opcode[2:4])

    elif asm_ins == "inc" or asm_ins == "dec":
        ### Printing Address
        print(address + ":",end = "\t")
        address = int(address,16)
        i = 0

        left_string = ""
        if asm_ins == "inc":
            inc(all_registers[asm_line[0]])
            opcode_inc_dec = '0x40'
            mid_part = "000"
        else:
            dec(all_registers[asm_line[0]])
            opcode_inc_dec = '0x48'
            mid_part = "001"

        if asm_line[0] in reg32Bit:
            reg_num = reg32Bit[asm_line[0]]
        elif asm_line[0] in reg16Bit:
            reg_num = reg16Bit[asm_line[0]]
            left_string = "66 "
            i = 1
        elif asm_line[0] in reg8Bit:
            reg_num = reg8Bit[asm_line[0]]
            i = 1
            left_string = "FE "
            hex_code = "11" + mid_part + reg_num
            hex_code = str(hex(int(hex_code,2))[2:])

            ## Printing Opcode
            print(left_string + hex_code[:2] + " " + hex_code[2:4] )
            
            address = address + 1 + i
            address = hex(address)
            address = address[2:]
            for j in range(16 - len(address)):
                address = '0' + address
            address = "0x" + address

            continue
        else:
            print("ERORR!!!")
            continue
        opcode_inc_dec = int(opcode_inc_dec,16)
        reg_num = int(reg_num,2)
        opcode = str(hex(opcode_inc_dec + reg_num))
        opcode = str(hex(int(opcode,16))[2:])

        ## Printing Opcode
        print(left_string + opcode)

        ## Calculating The Adress
        address = address + 2 + i
        address = hex(address)
        address = address[2:]
        for j in range(16 - len(address)):
            address = '0' + address
        address = "0x" + address
        
    elif asm_ins == "push" or asm_ins == "pop":
        
        print(address + ":",end = "\t")
        address = int(address,16)
        i = 0

        left_string = ""
        if asm_ins == "push":
            opcode_push_pop = 80
            #push()
        else:
            opcode_push_pop = 88
            #pop()
        
        if asm_line[0] in reg32Bit:
            reg_num = reg32Bit[asm_line[0]]
        elif asm_line[0] in reg16Bit:
            reg_num = reg16Bit[asm_line[0]]
            left_string = "66 "
            i = 1
        else:
            print("ERROR!!!")
            continue
        reg_num = int(reg_num,2)
        opcode = opcode_push_pop + reg_num
        opcode = str(hex(opcode)[2:])

        ## Printing Opcode
        print(left_string + opcode)
        
        ## Calculating The Address
        address = address + 1 + i
        address = hex(address)
        address = address[2:]
        for j in range(16 - len(address)):
            address = '0' + address
        address = "0x" + address

    elif asm_ins == "jmp":
        #jmp()

        ## Printing Opcode and Calculating The Address
        print(address + ":",end = "\t")
        address = int(address,16)
        current = label[asm_line[0]]
        jmp_bit = current - address
        opcode = str(hex(jmp_bit)[2:])
        print("eb" , opcode)
        address_list += [address]
        address = address + 2
        address = hex(address)
        address = address[2:]

    else:
        print("Error!!!")
        continue

###   End Of Processing   ###