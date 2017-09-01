#Matthew Siegel
#9/1/17
#Slope.py - Finding the slope of a line

x1 = int(input("x1"))
y1 = int(input("y1"))
x2 = int(input("x2"))
y2 = int(input("y2"))
slope = (y2-y1)/(x2-x1)
b = y1 - (slope * x1)
print("The slope is" , slope)
print("The equation for the line is Y =", slope, "x +",b)
