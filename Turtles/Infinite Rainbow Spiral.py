import turtle 
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow',  "magenta", "white", "black", "maroon"] 
s.bgcolor('black') 
t.speed('fastest')
t.shape("turtle")
while True:
  for x in range(999999999999999): 
    t.pencolor(colors[x%len(colors)])
    t.width(x/100 + 1)
    t.forward(x) 
    t.left(59)
