import math

xPointA = float(input("Введиде координату x: "))
yPointA = float(input("Введиде координату y: "))
xPointB = float(input("Введиде координату x1: "))
yPointB = float(input("Введиде координату y1: "))

AB = math.sqrt((xPointB-xPointA)**2 + (yPointB-yPointA)**2)
print(f"Расстояние между точками равно : {round(AB,2)}")
