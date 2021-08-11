import math
print("a*(x^2) + b*x + c = 0")

firstnumber = float(input("adad aval ro vared kon"))
number2 = float(input("adad dovom ro vared kon"))
number3 = float(input("adad sevom ro vared kon"))

a = math.sqrt((number2 ** 2) - (4 * firstnumber* number3))

if a > 0:
    print("javab aval hast", ((-1 * number2) + a) / (2 * firstnumber))
    print("javab dovom hast", ((-1 * number2) - a) / (2 * firstnumber))
elif a == 0:
    print("javab hast", (-1 * number2) / (2 * firstnumber))
else:
    print("bedeon javab")