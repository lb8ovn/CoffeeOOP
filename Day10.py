def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math = {"+":add,"-":subtract,"*":multiply,"/":divide}
num1 = int(input("First number "))
num2 = int(input("Second number "))
for x in math:
    print(x)
operation = input("Symbol ")
calculation = math[operation]
answer = calculation(num1,num2)
print(f"{num1} {operation} {num2} = {answer}")