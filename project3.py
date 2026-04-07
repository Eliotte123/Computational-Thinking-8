import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 50
x2 = -300
y2 = -50
x3 = -300
y3 = 150
x4 = -300
y4 = -150

# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("hawaii")
t1 = create_sprite("fish",x1,y1)
t2 = create_sprite("fish",x2,y2)
t3 = create_sprite("fish",x3,y3)
t4 = create_sprite("fish",x4,y4)


# Section 3 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - explain here which sprites are faster or slower
# The sprite x1 is the fastest because the random number range is the highest,
# and the slowest sprite is x2 because it has the lowest number range
for i in range(30):
    x1 += random.randint(1,50)
    x2 += random.randint(1,16)
    x3 += random.randint (1,34)
    x4 += random.randint (1,25)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# Section 4 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("player 4 wins!")

turtle.exitonclick()