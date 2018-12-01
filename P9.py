for a in range(2, 1000):
    for b in range(2, 1000):
        c = (a**2 + b **2) ** 0.5
        if float(c) == int(c):
            if a+b+c == 1000:
                print(a, b, c)
                print(int(a * b * c))
                quit()