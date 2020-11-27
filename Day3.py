print("gimmie an integer")
x = input()
try:
    x = int(x)
    if x % 2 == 0:
        print("That's an even number")
    else:
        print("That's an odd number")
    input("Press Enter")
except ValueError:
    print("Type an integer dumbass")

