import math

print ("Radius or Diameter?")
RorD = input()

if RorD == "r" or "rad" or "radius":
    print ("Please input radius:")
    radius = int(input())
    circum = 2 * math.pi * radius
elif RorD == "d" or "diameter":
    print ("Please input diameter")
    diameter = int(input())
    circum = math.pi * diameter

print (f"The Circumference equals: {circum}")