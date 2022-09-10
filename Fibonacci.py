for x in range(1, int(input("第n項"))+1):
    a = [1, 1]

    b = x+30
    for i in range(2, b):
        a.append(a[i-2]+a[i-1])
        i += 1

    for i in range(x, b):
        print(a[i] % a[i-x], end=" ")

    print("")
