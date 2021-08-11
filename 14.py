  
def a(b, c):
    for i in range(1, b+1):
        d = ""
        for e in range(1, c+1):
            f = e * i
            d += str(f) + ""
        print(d)            

b = int(input("vared kon adad aval ro"))
c = int(input("adad dovom ro vared kon"))

a(b, c)