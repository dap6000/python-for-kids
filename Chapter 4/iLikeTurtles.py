# Tell Python we want to use the turtle module using the import statement
import turtle

# Initizlize the turtle stuff, including setting up a blank canvas to draw on.
# The variable t gives us a way to talk to our turtle. You can think of it as
# representing the turtle in our code the same way the triangle icon represents
# the turtle on the screen.
t = turtle.Pen()

# We send messages to our tutle using functions called on the t variable.
t.forward(50)
# Here forward() means "move in the direction the triangle is pointing" and the
# paramater 50 tells the turtle how far we want it to move, measured in pixels.

# Now we'll turn our turtle.
t.left(90)
# The function name left() is straight forward enough. Just keep in mind terms
# like left and right are always relative (unlike terms like east and west). In
# this case left() is relative to the direction the turtle is facing. The
# paramater for left() is still a number but this time instead of telling the
# turtle how far to move forward measured in pixels we're telling the turtle
# how far to turn measured in degrees. By now you should have studied degrees
# in math class. There are 360 degrees in a circle. So if you did left(360) then
# the turtle would spin all the way around in place and end up facing the exact
# same direction. A 180 degree turn would put our turtle facing in the opposite
# direction. A 90 degree turn should make a square corner.

# Speaking of square corners, we'll now draw a square by moving 50 pixels and
# turning 90 degrees until we end up back where we started. So far we have drawn
# the line that will form the bottom of our square. That leaves 3 more sides. So
# we need to call t.forward(50) followed by t.left(90) 3 more times.
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

# Now we want to draw something else. First we need to reset the canvas.
t.reset()
# This function tells the turtle to erase everything it has drawn so far and
# move back to its default starting position in the center of the canvas. Since
# we drew a square last time the turtle ended up back where it began. Our turtle
# doesn't need to move at all to get back to the center of the canvas. We could
# have used t.clear() which tells the turtle to erase everything on the canvas
# but does NOT tell the turtle to return to the center of the screen.

# Last time we told the turtle to move using the forward() function. There is
# also a function called backward(). Can you guess what it does?
t.backward(100)
# The function forward(n) tells the turtle to move n pixels in the direction the
# triangle icon is pointing. And the function backward(n) tells the turtle to
# move n pixels in the direction oposite from where the triangle icon is
# pointing.

# The turtle also understands a pair of functions called up() and down(). These
# functions don't take any paramaters. And they don't have anything to do with
# direction on the canvas. Instead think of them as lifting the pen up from the
# canvas and back down again. When the pen is in the up position we can ove the
# turtle without drawing a line. When we want to start drawing again we put the
# pen back in the down position.
t.up()

# We can tell the turtle to turn to the right using the function right(n). Just
# like left(n) this function tells the turtle to turn n degrees, only this time
# it turns to its right rather than to its left. And remember the directions are
# alays relative to the direction the turtle is currently pointing.
t.right(90)

# Now we tell the turtle to move forward and turn again. But since we've lifted
# the pen up we won't draw a line while moving the turtle.
t.forward(20)
t.left(90)

# We have the turtle moved to where we want it to start drawing again so we put
# the pen back down and draw a line using the forward() function.
t.down()
t.forward(100)
