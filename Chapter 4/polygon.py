# I'm not going to do the programming puzzles at the end of chapter 4. I want
# you to try to figure those out on your own. But you're welcome to ask me for
# help. Instead of giving you my solutions to the programming puzzles I'm
# giving you a sneak peek at some of the topics the book will cover soon in
# future chapters. I've written a function (Chapter 7) that uses the turtle and
# some math to build a for loop (Chapter 6) to draw a polygon with the number
# of sides provided as a parameter.
import turtle

t = turtle.Pen()

def poly(sides) :
    t.reset()
    length = 800 / sides
    angle = 360.0 / sides
    for _ in range(0, sides) :
        t.forward(length)
        t.left(angle)

poly(3)
poly(4)
poly(5)
poly(6)
poly(7)
poly(8)
poly(9)
poly(10)
poly(11)
poly(12)
poly(13)
poly(14)
poly(15)
poly(16)
poly(17)
poly(18)
poly(19)
poly(20)
