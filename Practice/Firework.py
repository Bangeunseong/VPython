from vpython import *

rList = list()
objList = list()

ground = box(pos = vec(0,-5,0), size = vec(15,0.01,15))

for i in range(100):
    rList.append(vec(0,-4,0))
for r in rList:
    objList.append(sphere(pos = r, radius = 0.1, 
                          color = vec(random(),random(), random()), 
                          make_trail = True, retain = 30))
vi = vec(0,5,0)
a = vec(0,-3,0)
explosion = False

for obj in objList:
    obj.v = vi

t = 0
dt = 0.01

while t < 12:
    rate(1/dt)
    if t > 1 and explosion == False:
        print("Explosion!")
        explosion = True
        for obj in objList:
            vp = vec(random() - 0.5, random() - 0.5, random() - 0.5)
            obj.v += vp
    for obj in objList:
        obj.v += a*dt
        obj.pos += obj.v*dt
        if obj.pos.y < ground.pos.y:
            obj.pos.y = ground.pos.y
            obj.v.y = -0.8*obj.v.y
            obj.color = vec(random(), random(), random())
    t += dt
        