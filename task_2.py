import turtle
import math

def draw_tree(t, length, angle, depth):
    if depth == 0:
        return

    # Draw the main trunk (brown color)
    t.forward(length)
    t.left(angle)

    # Recursive call for the left branch
    draw_tree(t, length * 0.7, angle, depth - 1)

    t.right(2 * angle)

    # Recursive call for the right branch
    draw_tree(t, length * 0.7, angle, depth - 1)

    t.left(angle)
    t.backward(length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("brown")
    t.speed("fastest")

    # Positioning the turtle to start drawing
    t.left(90)
    t.penup()
    t.goto(0, -300)
    t.pendown()

    # Input for recursion depth
    depth = int(input("Enter the recursion depth: "))
    length = 150  # Length of the main trunk
    angle = 30    # Angle for branching

    # Draw the Pythagoras tree
    draw_tree(t, length, angle, depth)

    # Hide the turtle after drawing to clean up
    t.hideturtle()

    # Finish the drawing
    turtle.done()

if __name__ == "__main__":
    main()
