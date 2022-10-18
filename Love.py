import turtle as t
from turtle import*
def curve():
    for i in range(200):

        # Defining step by step curve motion
        t.speed(45)
        t.right(1)
        t.forward(1)
def f():
    fd(50)

def main():
    title("Hope")
    t.bgcolor("black")
    t.speed(45)
    t.fillcolor("red")
    t.begin_fill()
    t.left(45)
    curve()
    t.forward(100)
    t.left(295)
    t.forward(100)
    curve()
    t.forward(14)
    t.right(250)
    t.forward(20)
    t.hideturtle()
    t.end_fill()
    t.bgcolor("yellow")





if __name__ == '__main__':
    main()
