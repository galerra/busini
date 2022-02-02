def bus(a,b,c,d):
    if a in one:
        if a in gl:
            if b in sogl:
                if c in three and c != a and c!= b:
                    if d in gl and d != c and d != b:
                        return 1
        elif b in sogl:
            if b in gl:
                if c in three and c != a and c!= b:
                    if d in gl and d != c and d != b:
                        return 1

    return 0

one = ['C','D','E','G']
two = ['N','O','P']
three = ['A','B','E','G']
gl = ['A','E']
sogl = ['A','B','C','D','G']
print(bus('C','E','B','A'))