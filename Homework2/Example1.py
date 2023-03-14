from vpython import *

r = 1.1*6371000
G = 6.67e-11

earth = sphere(pos = vec(0,0,0), radius = 6371000, texture = textures.earth)
apple = sphere(pos = vec(0,r,0), radius = 300000, color = color.red)

earth.mass = 5.974e24
apple.mass = 0.086

F = G*earth.mass*apple.mass/r**2

earth.force = F
apple.force = -F

earth.acc = F/earth.mass
apple.acc = F/apple.mass

force_F = "{} = {} N"
acc_F = "{} = {} m/s^2"

print(force_F.format("earth.force", earth.force))
print(force_F.format("apple.force", apple.force))
print(acc_F.format("earth.acc", earth.acc))
print(acc_F.format("apple.acc", apple.acc))