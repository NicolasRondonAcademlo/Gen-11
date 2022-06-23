
from cmath import pi


price = int(input("Ingrea el precio "))
if price >= 300:
    price *= 0.7
elif price >= 200:
    price *= 0.8
elif price >=100:
    price *= 0.9
elif price < 100 and price >=0:
    price *= 0.95

print(f"El precio final es {price}")