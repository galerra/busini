from itertools import *
def bus(a, b, c, d):
    if a in gl:
        if b in sogl:
            if c in sogl and c != a and c != b:
                if d in gl and d != a:
                    return 1
    return 0
gl = ['A','E','I']
sogl = ['B','C','D']
verbs = 0
for i in permutations('ABCDEI',4):
    if bus(i[0],i[1],i[2],i[3]) == 1:
        verbs += 1
print(verbs)
