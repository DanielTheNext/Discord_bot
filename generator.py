import random

def gen_key():
    contraseña = ""

    unitext =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    for i in range(72):
        pre_contraseña = random.choice(unitext)
        contraseña += pre_contraseña

    print(contraseña)
