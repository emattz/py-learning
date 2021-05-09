import math

print("Radius or Diameter?")
RorD = input()


area = 0

if RorD == "r" or RorD == "rad" or RorD == "radius":
    print("Input Radius:")
    radius = int(input())
    area = math.pi * math.pow(radius, 2)
elif RorD == "d" or RorD == "dia" or RorD == "diameter":
    print("Input Diameter:")
    diameter = int(input())
    area = (math.pi / 4) * math.pow(diameter, 2)


print(f"Area is: {area}")