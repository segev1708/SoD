import math
power = float(input("to the power of "))
fromNum = int(input("from tier "))
toNum = int(input("to tier "))
res = 0 
for n in range(fromNum,toNum+1):
    res = res + ((n+1)**power)
print(f"costs {res} powder")