def board(a, b):
    for i in range(a):
        c = ''
        for j in range(b):
            if (i % 2 == 0):
                if (j % 2 == 0):
                    c += '#'
                else:
                    c += '*'
            else:
                if (j % 2 == 0):
                    c+= '*'
                else:
                    c += '#'
        print(c)            

a = int(input('n: '))
m = int(input('m: '))

board(a, m)