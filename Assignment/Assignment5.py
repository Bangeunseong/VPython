from vpython import *

def keydownInput(evt):
    s = evt.key
    if 'down' in s:
        spring.ks = 12000

def keyupInput(evt):
    s = evt.key
    if 'down' in s:
        spring.ks = 6000

building_floor = box(pos = vec(-2.5,-0.05,0), size = vec(8,0.1,8), color = color.white)
scoreboard = box(pos = vec(-4,7.5,0), size = vec(0.5,15,0.5), color = color.cyan)
showwinner = label(pos = scene.center, text="Win!", box = False, visible = False, color = color.red)

spring = helix(pos = vec(0,5,0), axis = vec(0,-1,0), v = vec(0,0,0), m = 30, ks = 6000, radius = 0.1, rate = 0.05, degree = 0, thickness = 0.03, coils = 20, color = color.cyan)
pedalstep = box(pos = spring.pos, size = vec(1.4,0.05,0.5), color = color.orange)
center_piller = cylinder(pos = spring.pos, axis = vec(0,3,0), radius = 0.1, color = color.orange)
handle = cylinder(pos = spring.pos + center_piller.axis - vec(0.7,0,0), axis = vec(1.4,0,0), radius = 0.1, color = color.orange)

t = 0
dt = 0.001
r0 = 1
kd = 70
g = vec(0,-9.8,0)

scene.center = spring.pos
scene.bind("keydown", keydownInput)
scene.bind("keyup", keyupInput)

while True:
    rate(1/dt)
    if handle.pos.y > 15:
        showwinner.visible = True
        break
    Fg = spring.m*g
    Fnet = Fg
    if (spring.pos + spring.axis).y <= 0:
        rhat = norm(spring.axis)
        s = r0 - mag(spring.axis)
        Fspr = -spring.ks*s*rhat
        Fdamp = -kd*dot(spring.v, rhat)*rhat
        Fnet = Fnet + Fspr + Fdamp

    spring.v += Fnet/spring.m*dt
    spring.pos += spring.v*dt
    if spring.pos.y < 1:
        spring.axis = -norm(spring.pos)*mag(spring.pos)
    else:
        spring.axis = -norm(spring.pos)
    pedalstep.pos = spring.pos
    center_piller.pos = spring.pos
    handle.pos = spring.pos + center_piller.axis - vec(0.7,0,0)
    t += dt