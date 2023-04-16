from vpython import *

t = 0
dt = 0.001
G = 9.8

rock = sphere(pos = vec(0,0,0), v = vec(9.6,7.2,0), radius = 0.5, color = color.white)
monkey = sphere(pos = vec(12,9,0), v = vec(0,0,0), radius = 0.5, color = color.red)
g = vec(0,-G,0)

while mag(rock.pos - monkey.pos) > rock.radius + monkey.radius:
    rate(1/dt)

    rock.v += g*dt
    rock.pos += rock.v*dt
    monkey.v += g*dt
    monkey.pos += monkey.v*dt
    
    t += dt