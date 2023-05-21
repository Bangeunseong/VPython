from vpython import *

toycar = box(pos=vec(0,0,0), size=vec(0.1,0.1,0.1), v=vec(0,0,0), m = 1, color=color.red)
wall = box(pos=vec(5 + 0.1,0,0), size=vec(0.05,2,2), color=color.white)


t = 0
dt = 0.001

while mag(toycar.pos) < mag(wall.pos):
    rate(1/dt)
    #F = vec(1 + 0.8*toycar.pos.x,0,0)
    F = vec(1 + 0.16*toycar.pos.x**2,0,0)
    toycar.v += F/toycar.m*dt
    toycar.pos += toycar.v*dt
    t += dt

print("Velocity :", mag(toycar.v), "m/s")
print("Kinetic Energy :", 1/2*toycar.m*mag(toycar.v)**2, "J")
print("Work :", (1+5)*5/2, "N.m")