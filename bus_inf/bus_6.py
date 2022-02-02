def bus(a,b,c,):
    if a in one:
        if a in sogl:
            if b in gl:
                if c in sogl and c != 'V':
                    return 1
        if a in gl:
            if b in sogl:
                if c in gl and c != 'V':
                    return 1
    return 0

one = ['A','G','E']
two = ['N','O','P']
three = ['A','B','E','G']
gl = ['A','E']
sogl = ['B','V','G','D']
print(bus('G','E','B'))