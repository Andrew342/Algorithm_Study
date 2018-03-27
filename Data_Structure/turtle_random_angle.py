import random
import turtle

def tree(branch_len,t):
    if branch_len>5:
        t.forward(branch_len)
        right_angle=random.randint(15,45)
        t.right(right_angle)
        tree(branch_len-15,t)
        t.left(2*right_angle)
        tree(branch_len-15,t)
        t.right(right_angle)
        t.backward(branch_len)

def main():
    t=turtle.Turtle()
    my_win=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    my_win.exitonclick()

main()
