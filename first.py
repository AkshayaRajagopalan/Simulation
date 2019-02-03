from visual import *
ball = sphere(pos=(0,10,0), radius=1, color=color.red)
dt = 0.1
ball.velocity = vector(0,0,0)
t=0

while (t < 10000):
    rate(10)
    ball.pos.y = 15*sin(t)
    ball.pos.x = 30*cos(t)
    t = t+dt
