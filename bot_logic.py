import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        final_pass = random.choice(elements)

        password += final_pass

    return password

def practice_math():
    num0 = random.randint(1, 100)
    num1 = random.randint(1, 100)
    
    op = random.randint(1, 3)

    var0 = str(num0) + " + " + str(num1)
    var1 = str(num0) + " * " + str(num1)
    var2 = str(num0) + " / " + str(num1)
    
    if op == 1:
        return var0

    if op == 2:
        return var1

    if op == 3:
        return var2
