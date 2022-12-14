min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))
x: int = 0

for i in range(min, max, 1):
    if i%2 != 0 and i%3 == 0:
        x = x + i
print(f"{x} 3-mal osztható páratlan szám van")
