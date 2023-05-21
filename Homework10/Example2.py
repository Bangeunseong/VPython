from vpython import *

spring = helix(pos = vec(0,0,0), axis = vec(0.2,0,0), color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)
block = box(pos = vec(3,0,0), size = vec(0.1,0.1,0.1), v = vec(-1,0,0), m = 2, color = color.red)

ks = 500
r0 = 0.2

t = 0
dt = 0.001

def collided(spring, block):
    if mag(spring.axis) >= mag(block.pos):
        return True
    return False

while True:
    rate(1/dt)
    if collided(spring, block):
        s = r0 - mag(block.pos)
        Fs = ks*s*norm(block.pos)
        block.v += Fs/block.m*dt
        block.pos += block.v*dt
        spring.axis = block.pos
    else:
        block.pos += block.v*dt

    if mag(block.v) < 0.03:
        break
    t += dt

print("Travel Distance :", r0 - mag(block.pos))
print("Travel Distance(Calculated by formula) :", sqrt(0.004))