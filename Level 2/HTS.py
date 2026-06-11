import turtle
import random
import time

t = turtle.Turtle()
t.shape('square')
t.color("black")

n_foods = 10
list_of_foods = []

for kk in range(n_foods):
    food = turtle.Turtle()
    food.penup()
    food.speed(0)
    food.shape("square")
    food.color("blue")
    food.goto(random.randint(-200, 200), random.randint(-200, 200))
    list_of_foods.append(food)

pen = turtle.Turtle()
pen.penup()
pen.goto(180, 180)
pen.color("white")
pen.ht()

report = turtle.Turtle()
report.penup()
report.goto(0, 0)
report.color("white")
report.ht()

started = 0

def right():
    if t.heading() != 180.0:
        t.setheading(0.0)

def left():
    if t.heading() != 0.0:
        t.setheading(180.0)

def up():
    if t.heading() != 270.0:
        t.setheading(90.0)

def down():
    if t.heading() != 90.0:
        t.setheading(-90.0)

steps = 0

ts = t.screen
ts.bgcolor("khaki")

ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()

caught = [False] * n_foods
segments = []
game_over = False

# --- BONUS IDEA #5: DRAW THE BOUNDARY LINE ---
boundary_drawer = turtle.Turtle()
boundary_drawer.ht()
boundary_drawer.penup()
boundary_drawer.goto(-250, -250)
boundary_drawer.pendown()
boundary_drawer.color("red")
boundary_drawer.pensize(3)
for _ in range(4):
    boundary_drawer.forward(500)
    boundary_drawer.left(90)

while game_over == False:
    steps = steps + 1
    pen.write(len(segments), align="center", font=("Courier", 24, "normal"))
    
    for kk in range(len(list_of_foods)):
        if not caught[kk]:          
            if t.distance(list_of_foods[kk]) < 20:
                caught[kk] = True
                # --- BONUS IDEA #4: Give a distinct color to the food once eaten ---
                list_of_foods[kk].color('red') 
                segments.append(list_of_foods[kk])
                pen.clear()

    # Move the end segment in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = t.xcor()
        y = t.ycor()
        segments[0].st()
        segments[0].goto(x, y)
    
    t.forward(20)
    
    # --- BONUS IDEA #5: BOUNDARY CHECK ---
    # If the snake head goes outside the (-250, 250) box, game over.
    if abs(t.xcor()) > 250 or abs(t.ycor()) > 250:
        game_over = True
        time.sleep(0.5)
        t.clear()
        t.ht()
        for food_item in list_of_foods:
            food_item.ht()
        report.color("red")
        report.write("GAME OVER: Out of Bounds!", align="center", font=("Courier", 24, "bold"))
        break # Exit the game loop immediately

    if t.xcor() > 10:
        started = 1
        
    if len(segments) == n_foods:
        if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
            game_over = True
            time.sleep(1)
            t.clear()
            t.ht()
            for kk in range(len(segments)):
                segments[kk].ht()
                
            report.write("Steps Taken: " + str(steps), align="center", font=("Courier", 24, "normal"))
    
    time.sleep(0.1)

ts.mainloop()