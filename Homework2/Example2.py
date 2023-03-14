from vpython import *

r = 200
G = 6.67e-11

man1 = sphere(pos = vec(0,0,0), radius = 50, color = color.white)
man2 = sphere(pos = vec(r,0,0), radius = 50, color = color.blue)

man1.mass = 60
man2.mass = 75

F = G*man1.mass*man2.mass/r**2

man1.force = F
man2.force = -F
man1.acc = F/man1.mass
man2.acc = F/man2.mass

f_format = "{} = {} N"
acc_format = "{} = {} m/s^2"

#Cannot detect force or acceleration
#Acceleration of man2 = 1.0005e-13 m/s^2
#Force of man2 = 7.50375e-12 N
print(f_format.format("man1.force", man1.force))
print(f_format.format("man2.force", man2.force))
print(acc_format.format("man1.acc", man1.acc))
print(acc_format.format("man2.acc", man2.acc))