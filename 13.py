a = int(input('First number is '))
b = int(input('Second number is '))
c = max(a, b)
d = min(a, b)

for i in range(1, (c * d)):
    if ((c * i) % d == 0):
        answer = (c * i)
        break
        
print(answer)