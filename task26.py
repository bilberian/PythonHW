# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('insert a: '))
b = int(input('insert b: '))

def recf(a, b):
    if(b == 0):
        return 1; 
    if(b == 1):
        return a; 
    return a * recf(a, b - 1)

print(recf(a, b))
