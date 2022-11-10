#Write a Python program which accepts the radius of a circle from the user and compute the area.
#Sample Output :
#r = 1.1
#Area = 3.8013271108436504

import math
radius = float(input("input radius value: "))
x = 0
while x == 0:
    if radius == 0:
        print("input error!")
        radius = float (input("input radius value: "))
    else:
        break
print("circle area is: ")
print((math.pi)*float (radius)**2)
