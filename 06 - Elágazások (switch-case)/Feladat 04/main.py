from os import system

print("Kérem az első számot: ")
a = int(input(""))
print("Kérem a második számot: ")
b = int(input(""))
print("Kérem a műveletet:" )
c = str(input("")).strip()

system('cls')

match c:
    case "/":
        print(f"{a / b}")
    case "*":
        print(f"{a / b}")
    case "+":
        print(f"{a / b}")
    case "-":
        print(f"{a / b}")
    case _:
        print(f"Valamelyik adat érvénytelen")