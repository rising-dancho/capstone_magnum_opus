import turtle

# use loop to create a stairs with 5 steps
# create function: stairs(size, nb)
# t

t = turtle.Turtle()

def stairs(size, steps):
    count = 0
    for i in range(0,steps):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
        # size -= 10 # decrement
    t.forward(size)

def square(size):
    for i in range(0,4):
        t.forward(size)
        t.left(90)

def squares():
    # 10/ 20/ 30/ 40
    # size = (i+1)*beinning_size
    ...

# stairs(100, 5)
square(100)
square(50)

turtle.done()

