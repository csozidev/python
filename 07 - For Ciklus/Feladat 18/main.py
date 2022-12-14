min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))
x: int = 0

for i in range(min, max, 1):
    if min%2 == 0:
        if i%2 == 0:
            x = x + i
        else:
            x = x - i
    else:
        if i%2 == 0:
            x = x - i
        else:
            x = x + i
print(f"{x} a végeredmény")