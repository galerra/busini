def bus(a,b,c):
    if b in two:
        if a in one and a != b:
            if (a in gl and c in gl) or (a in sogl and c in sogl) :
                return 1
    return 0

one = ['M','N','O']
two = ['N','O','P']
three = ['A','C','D']
gl = ['O','U']
sogl = ['M','N','P']
print(bus('N','O','N'))