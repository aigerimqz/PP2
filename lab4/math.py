import math
#ex 1
# deg = float(input("Input degree: "))
# rad = math.radians(deg)
# print("Output radian:", round(rad, 6))


#ex 2
# height = float(input("Height: "))
# base1 = float(input("Base, first value: "))
# base2 = float(input("Base, second value: "))
# area = height*(base1 + base2)*(1/2)
# print(area)


#ex 3
# sides = int(input("Input the number of sides: "))
# length = float(input("Input the length of a side: "))
# r = length/(2*math.tan(math.radians(180/sides)))
# p = sides * length
# area = (p * r)/2
# print("The area of the polygon is:", round(area, 2))

#ex 4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print(area)