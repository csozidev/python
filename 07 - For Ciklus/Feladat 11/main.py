min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))
os: int = 0
atlan: int = 1

for i in range(min, max, 1):
    if i%2 == 0:
        os += i
    else:
        atlan = atlan * i
print(os)
print(atlan)