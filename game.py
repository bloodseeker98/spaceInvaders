import turtle
import os
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.lt(90)

playerspeed = 15  # changeable




#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed = 2



#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.5,.5)
bullet.hideturtle()

bulletspeed = 20

#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bullet state as a global if it needs changed
    global bulletstate
    if(bulletstate != "ready"):
        return

    #Move the bullet to jsut above the player
    x = player.xcor()
    y = player.ycor()+10
    bullet.setposition(x,y)
    bullet.showturtle()
    bulletstate = "fire"

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if(distance<16):
        return True
    else:
        return False

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")


#Main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x+=enemyspeed
        if x > 280 or x < -280:
            enemyspeed *= -1
            enemy.sety(enemy.ycor()-40)
        enemy.setx(x)
        # check collision
        if (isCollision(bullet, enemy)):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        if enemy.ycor() <= player.ycor():
            player.hideturtle()
            enemy.hideturtle()
            print('Game Over')
            turtle.exitonclick()
            break



    #Move the bullet
    if(bulletstate == "fire"):
        y = bullet.ycor()
        y+= bulletspeed
        bullet.sety(y)
         #check to see if the bullet has gone to the top
        if y > 275:
            bulletstate = "ready"
            bullet.hideturtle()





# delay = input("Enter to continue")