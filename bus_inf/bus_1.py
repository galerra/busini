def bus(a,b,c):
    if a in one:
        if b in two:
            if c in three and c != a and c!= b:
                return 1
    return 0

one = ['M','N','O']
two = ['L','M','O']
three = ['L','M','N']
print(bus('M','N','O'))