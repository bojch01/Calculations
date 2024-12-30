import math

#finds area of circle
def circle():
    try:
        radius = float(input("Great you chose circle! What is the radius? "))
        pi = math.pi
        area = radius * radius * pi
        return f"The area of the circle is {area:.1f}"
    except ValueError:
        return "Input is invalid. Enter numerical values only."

#finds area of rectangle
def rectangle():
    try:
        length = float(input("Great you chose rectangle! What is the length? "))
        width = float(input("What is the width?"))
        area = length * width
        return f"The area of the rectangle is {area:.1f}"
    except ValueError:
        return "Input is invalid. Enter numerical values only."

#finds area of triangle
def triangle():
    try:
        height = float(input("Great you chose triangle! What is the height? "))
        base = float(input("What is the base? "))
        area = 0.5 * base * height
        return f"The area of the triangle is {area:.1f}"
    except ValueError:
        return "Input is invalid. Enter numerical values only."

#finds area of trapezoid
def trapezoid():
    try:
        baseOne = float(input("Great you chose trapezoid! What is the length of the first base? "))
        baseTwo = float(input("What is the length of the second base? "))
        height = float(input("What is the height? "))
        area = (baseOne + baseTwo) * height / 2
        return f"The area of the trapezoid is {area:.1f}"
    except ValueError:
        return "Input is invalid. Enter numerical values only."

#finds the shape user is referring to
def get_shape(shape):
    switch = {
        'circle': circle,
        'rectangle': rectangle,
        'triangle': triangle,
        'trapezoid': trapezoid,
    }
    #ensures the input is not case-sensitive
    shape_function = switch.get(shape.lower())
    #checks if the shape has a switch case
    if shape_function:
        return shape_function()
    else:
        return switch.get(shape, 'That shape is not available, choose one the following: circle, rectangle, triangle, '
                             'or trapezoid.')

#shown in console (main program)
shape = input("What shape would you like to find the area of? ")
print(get_shape(shape))
