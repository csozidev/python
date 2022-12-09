min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))
x: int = 0

for i in range(min, max, 1):
    x += i
print(x)