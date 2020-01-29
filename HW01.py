def classify_triangle(x,y,z):
    """This is a function that takes in 3 values and returns if it is a triangle and if it is equilateral or isosceles or right"""
    #this program is wantedly bugged so that we can test prove that testing is important
    if(x+y<z or y+z<x or x+y<z or x<0 or y<0 or z<0):
        return "not a triangle"
    if(x==y==z):
        return "equilateral triangle"
    elif(x==y or y==z or x==z):
        return "isosceles triangle"
    elif(x*x==y*y+z*z):
        return "right triangle"
    elif(y*y==x*x+z*z):
        return "right triangle"
    elif(z*z==x*x+y*y):
        return "right triangle"
    elif(x!=y!=z):
        return "scalene triangle"