# This is a sample Python script.

def classify_triangle_function(a, b, c):
    type = ""
    if a == b and a == c and b == c:
        type += "Given triangle is Equilateral triangle."
        # Any two sides are equal -> Isosceles triangle
    elif a == b or a == c or b == c:
        type += "Given triangle is Isosceles triangle."
    else:
        type += "Given triangle is a Scalene triangle."
        # Checking for right angle triangle
        if (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b):
            type += " and it is a right triangle."
        else:
            type += " and not a right triangle."

    return type


print("Please enter value of side a :-")
a = int(input())

print("Please enter value of side b :-")
b = int(input())

print("Please enter value of side c :-")
c = int(input())

print(classify_triangle_function(a, b, c))