from os import system

print("Milyen üdítőt kér?")
drink = int(input(""))

system('cls')

match drink:
    case 1:
        print("Ön Coca-Colát választott")
    case 2:
        print("Ön Pepsit választott")
    case 3:
        print("Ön Fantát választott")
    case 4:
        print("Ön Spritot választott")