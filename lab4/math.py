#task1
import math
pi=3.1415926535
degree=int(input("degree: "))
a=degree*pi/180
print(a)

#task2
import math
height=int(input("height: "))
first=int(input("first value: "))
second=int(input("second value: "))
S=(first+second)*height/2
print("Expected Output: ", S)

#task3
import math
def areapolygon():
    sides = int(input("Input number of sides: "))
    length = int(input("Input the length of a side: "))

    p = sides * length
    a = length/(2*math.tan(math.pi/sides))
    return p*a/2

area = areapolygon()
print(area)

#task4
def paralellogram():
    length = int(input("Length of base: "))
    height = int(input("Height of parallelogram: "))
    result = "Expected Output: "+str(height*length)
    return result

area_parallelogram=paralellogram()
print(area_parallelogram)