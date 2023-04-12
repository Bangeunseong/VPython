from vpython import *

s_r = 3.5e10
e_r = 6.4e9
G = 6.67e-11

t = 0
mem_t = 0
dt = 24 * 3600

sun = sphere(pos = vec(0,0,0), radius = s_r, v = vec(0,0,0), mass = 1.99e30, color = color.red)
earth = sphere(pos = vec(0,1.5e11,0), radius = e_r, v = vec(-29783,0,0), mass = 5.97e24, texture = textures.earth)
attach_trail(earth, radius = 2.4e9, color = color.white, pps = 50)

while True:
    rate(60)
    r = earth.pos - sun.pos
    origin_pos_x = earth.pos.x

    earth.f = -G*sun.mass*earth.mass/mag(r)**2*norm(r)
    sun.f = -earth.f

    earth.v += earth.f/earth.mass*dt
    sun.v += sun.f/sun.mass*dt
    earth.pos += earth.v*dt
    sun.pos += sun.v*dt
    
    t += dt
    if(origin_pos_x > 0 and earth.pos.x < 0):
        print(t/dt - mem_t)
        mem_t = t/dt
    