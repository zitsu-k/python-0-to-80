import math


radius = int(input("entre the radius of the circle?:"))

# circumference_of_circle= input(f"the circumference of the circle is {radius*2*22/7} cm^2")
circumference_of_circle= 2*math.pi*radius

result = round(circumference_of_circle)

print(f"The circumference of the circle is:{result} cm^2")








