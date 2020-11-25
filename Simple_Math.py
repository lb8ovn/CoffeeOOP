def additup(number):
    total = 0
    for num in range(number+1):
        total = num + total
    print(total)

additup(100)