def bus(a,b,c):
    if a in one:
        if a == 'A':
            if b == 'B'or b =='C' or b == 'D':
                if c in three and c != b and c!= a:
                    return 1
        else:
            if b == 'A' or b == 'E':
                if c in three and c != b and c!= a:
                    return 1
    return 0

one = ['A','B','D']
two = ['N','Б','В']
three = ['A','C','D']
print(bus('B','A','D'))