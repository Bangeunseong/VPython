from vpython import *

def keydownInput(evt):
    s = evt.key
    rate = 1
    if 'down' in s:
        spring.ks = 11000
    elif 'left' in s and spring.degree < 15:
        spring.axis.rotate(angle=radians(rate))
        spring.rotate(angle=radians(rate), axis=vec(0,0,1))
        pedalstep.rotate(angle=radians(rate), axis=vec(0,0,1))
        center_piller.rotate(angle=radians(rate), axis=vec(0,0,1))
        handle.rotate(angle=radians(rate), axis=vec(0,0,1))
        spring.degree += rate
    elif 'right' in s and spring.degree > -15:
        rate *= -1
        spring.axis.rotate(angle=radians(rate))
        spring.rotate(angle=radians(rate), axis=vec(0,0,1))
        pedalstep.rotate(angle=radians(rate), axis=vec(0,0,1))
        center_piller.rotate(angle=radians(rate), axis=vec(0,0,1))
        handle.rotate(angle=radians(rate), axis=vec(0,0,1))
        spring.degree += rate



def keyupInput(evt):
    s = evt.key
    if 'down' in s:
        spring.ks = 8000

building_floor = box(pos = vec(-2.5,-0.05,0), size = vec(15,0.1,15), color = color.white)

spring = helix(pos = vec(0,5,0), axis = vec(0,-1,0), v = vec(0,0,0), m = 30, ks = 8000, radius = 0.1, rate = 0.05, degree = 0, thickness = 0.03, coils = 20, color = color.cyan)
pedalstep = box(pos = spring.pos, size = vec(1.4,0.05,0.5), color = color.orange)
center_piller = cylinder(pos = spring.pos, axis = vec(0,3,0), radius = 0.1, color = color.orange)
handle = cylinder(pos = spring.pos + center_piller.axis - vec(0.7,0,0), axis = vec(1.4,0,0), radius = 0.1, color = color.orange)
busted = label(pos = scene.center, text="<b>Busted!</b>", box = False, visible = False, height = 30, color = color.red)

t = 0
dt = 0.01
r0 = 1
kd = 30
g = vec(0,-9.8,0)


scene.bind("keydown", keydownInput)
scene.bind("keyup", keyupInput)

while True:
    rate(1/dt)
    Fg = spring.m*g
    Fnet = Fg
    if (spring.pos + spring.axis).y <= 0.01:
        rhat = norm(spring.axis)
        s = r0 - spring.pos.y
        if s > r0:
            busted.visible = True
            break
        Fspr = -spring.ks*s*rhat
        Fdamp = -kd*dot(spring.v, rhat)*rhat
        Fnet = Fnet + Fspr + Fdamp

    spring.v += Fnet/spring.m*dt
    spring.pos += spring.v*dt
    if spring.pos.y <= 1:
        spring.axis = norm(spring.axis)*spring.pos.y
    else:
        spring.axis = norm(spring.axis)
    pedalstep.pos = spring.pos
    center_piller.pos = spring.pos
    handle.pos = spring.pos + center_piller.axis - vec(0.7,0,0)
    scene.center = spring.pos
    busted.pos = spring.pos
    t += dt