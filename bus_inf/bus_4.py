def bus(a,b,c):
    if a in one:
        if b in two:
            if c in three and c != b and c!= a:
                return 1
    return 0

one = ['А','В','Г']
two = ['А','Б','В']
three = ['Б','В','Г']
print(bus('Б','Г','В'))