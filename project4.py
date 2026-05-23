from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("hawaii")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
aliens = 0
rockets = 0
cost = 0


# OPTIONAL: use this invisible alien to say a message

m1 = create_sprite("alien", -200,200)
m1.hideturtle()




# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_aliens():
    global aliens
    aliens += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("alien.gif",x,y)

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
def get_rocket():
    global aliens, rockets, cost
    if aliens >= cost:
        cost = cost * 4
        rockets += 1
        x = -400 + 120* rockets
        y = -250
        create_sprite("rocket.gif",x,y)

window.onkeypress(get_aliens, "space")
window.onkeypress(get_rocket, "r")








# Section 3 - game loop
window.listen()
for i in range(1000000000):
    m1.clear()
    m1.write(f"Aliens: {aliens}\nCost: {cost}\nRockets: {rockets}",font=("Arial", 15, "normal"))

    #if i % 100 == 0:
    #    aliens += 1*rockets

    cost = rockets*2
    
    # TODO - put any automatic actions here

    
    


    # OPTIONAL - use the message sprite to say a message
    # m1.clear()
    # m1.write("Hello")

    # The goal of the game is to purchase rockets. To get rockets, 
    # you must press the space bar to generate aliens, and every time you purchase a rocket, the cost goes up by two.
    