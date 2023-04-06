from vpython import *
import random as rand
import time as time
#Method
def on_keydown(event):
    global plane
    if event.key == "left" and plane.pos.x > -9:
        plane.pos.x -= 0.5
    elif event.key == "right" and plane.pos.x < 9:
        plane.pos.x += 0.5
    elif event.key == "up" and plane.pos.y < 9:
        plane.pos.y += 0.5
    elif event.key == "down" and plane.pos.y > -9:
        plane.pos.y -= 0.5

scene = canvas(width = 800, height = 600)
scene.range = 10
scene.title = "Dodge Game"
scene.bind("keydown", on_keydown)

#Fields of background, bullets, plane
t = 0
dt = 0.0001

background = box(pos = vec(0,0,-0.5), size = vec(18,18,0), color = color.black)
plane = box(pos = vec(0,-8,0), size = vec(1,1,1), color = color.green)
bulletList = []

#Main
startTime = time.time()
while True:
    rate(1/dt)
    if time.time() - startTime > 5 or t == 0:
        startTime = time.time()
        bulletList.append(sphere(pos = vec(rand.uniform(-9, 9), 9, 0), v = vec(0, rand.uniform(5,9), 0), radius = 0.5, color = color.red))
        
    for bullet in bulletList:
        if mag(bullet.pos - plane.pos) < 1:
            label(pos = vec(0,0,0), text = "Game over!",height = 30, color = color.red, box = False)
            exit()
        if bullet.pos.y < -9:
            bullet.pos = vec(rand.uniform(-9, 9), 9, 0)
            bullet.v = vec(0,rand.uniform(2, 4),0)
        bullet.pos -= bullet.v*dt
    t += dt