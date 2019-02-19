from visual import *

scene = display(width = 600, height = 600, center = (0,5,0))

sun = sphere(pos=(0,0,0), radius=100, color = color.orange)
earth = sphere(pos=(-200,0,0), radius=10, materials = materials.earth,
               make_trail = true)

earthv = vector(0,0,5)

for i in range(10000):
    rate(100)
    earth.pos = earth.pos + earthv
    dist = (earth.x**2 + earth.y**2 + earth.z**2)**0.5
    RadialVector = (earth.pos - sun.pos)/dist
    Fgrav = -10000*RadialVector/dist**2
    earthv = earthv + Fgrav
    earth.pos += earthv
    if dist <= sun.radius: break
