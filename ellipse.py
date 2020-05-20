


import turtle
import math


def ellipse(a, b, angle, unit):
    if unit == "d":
        r = (angle * 0.875)
        draw(a, b, r)
    elif unit == "r":
        r = (angle * 0.875 * 57.296)
        draw(a, b, r)
    else:
        print("!!! Invalid Syntax !!!")
        print('''
Eg : ellipse(a=250, b=100, angle=6.28319, unit="r")    #for angle in radian
Eg : ellipse(250, 100, 6.28319, "r")    #for angle in radian

Eg : ellipse(a=250, b=100, angle=360, unit="d")    #for angle in degree
Eg : ellipse(250, 100, 360, "d")    #for angle in degree
''')

def draw(a, b, r):
    myturtle = turtle.Turtle()
    myturtle.hideturtle()
    
    for i in range(int(r)):
        if i == 0:
            myturtle.up()
        else:
            myturtle.down()
                    
        myturtle.setposition(a*math.cos(i/50), b*math.sin(i/50))
    myturtle.goto(0, 0)


ellipse(100, 50, angle=i, unit="d")
    
