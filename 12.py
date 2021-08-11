def a(num):
    b = 1
    c = 1
    d = 0
    while b <= num:
        if (b == num):
            d("bale")
            flag = 1
            break
        else:
            c += 1
            b *= c
            continue
    if d == 0:
        print("na")    
    
e = int(input("adad to hast"))
a(e)