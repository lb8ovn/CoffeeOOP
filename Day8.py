
def prime(number):
    y = False
    for x in range(2,number):
        if number%x == 0:
            y = True
    if y == True:
        print('Not a Prime')
    else:
        print('Prime')


