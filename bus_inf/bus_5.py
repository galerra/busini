def bus(a, b, c, d):
    if a == 'I' or a == 'F':
        if b == 'I' or b == 'L':
            if c == 'H' or c == 'L':
                if d == 'F' or d == 'H':
                    return 1
    return 0
print(bus('I', 'L', 'H', 'F'))