from vpython import *

#회전관성 = Icom + m*h^2
#Icom = 1/12*door.mass*(0.8**2 + 0.1**2)
#회전관성 = 1/12*door.mass*(0.8**2 + 0.1**2) + door*mass*(0.4**2)
#Torque = 0.75*10
#각가속도 = Torque/I

door = box(pos = vec(0,0,0), size = vec(4,0.1,8), angle = 0, w = vec(0,0,0), mass = 40, color = vec(0.6,0.2,0.2))

I = 1/12*door.mass*(0.8**2 + 0.1**2) + door.mass*(0.4**2)
F = 10
Torque = 0.75*F
A = Torque/I
axis = vec(0,0,1)

t = 0
dt = 0.01

scene.center = vec(-2,0,0)

while door.angle < radians(90):
    rate(1/dt)
    door.w += A*norm(axis)*dt
    dtheta = mag(door.w)*dt
    door.rotate(angle = dtheta, axis = norm(door.w), origin = vec(-2,0,0))
    door.angle += dtheta
    t += dt

print("Time :", t, "ms")
print("I :", I)