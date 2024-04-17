import turtle

t = turtle.Turtle()
t.shape("turtle")

scores = [90, 80, 70, 60, 50, 35, 100, 87, 65, 88]
colors = ["red", "green", "blue", "brown", "chartreuse", "cyan", "gold", "ivory", "LightSkyBlue", "navy"]

t.forward(320)

#t.up()
t.goto(-210, 0)
#t.down()

t.left(90)
t.forward(150)

t.up()
t.goto(-200, 0)
t.down()

for i in range(10):
    t.fillcolor(colors[i])
    t.begin_fill()
    if i != 0:
        t.right(90)
    t.forward(scores[i])
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(scores[i])
    t.right(90)
    t.forward(20)
    t.end_fill()
    t.up()
    t.goto(50*(i+1)-200, 0)
    t.down()

i = 0
while True:
    t.up()
    t.right(90)
    t.color(colors[i%10])
    i += 1