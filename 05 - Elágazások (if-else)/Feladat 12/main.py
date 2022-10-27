from os import system

number: int = None

print("Kérem a számot")
number = int(input(""))

system('cls')

if (number >= 10 and number <= 20):
    print("A szám 10 és 20 között van")
elif(number >= -20 and number <= -10):
    print("A szám -10 és -20 között van")
else:
    print("A szám nincsen se -10 és -20, vagy 10 és 20 között")