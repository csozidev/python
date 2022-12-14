min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))
x: int = 0
y: int = 0
avarage: float = 0

for i in range(min, max, 1):
    x = x + i
    y += 1
avarage = x / y
print(f"{avarage} A számok átlaga")