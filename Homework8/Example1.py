from vpython import *

#충돌하게 되는 최소 속력 = sqrt(mu*g*distance*2)
#distance = 20
#mu = 0.8, g = 9.8
#최소 속력은 17.70...


def drawBtn(b):
    b.disabled = True
    return b.disabled

def myVelocity():
    global car
    car.v = velocitySlider.value * vec(1,0,0)
    velocityText.text = velocitySlider.value

title = wtext(pos = scene.title_anchor, text = 'Car and Person Simulation')
btnDraw = button(pos = scene.title_anchor, text = 'Start', bind = drawBtn)
velocitySlider = slider(min = 0, max = 50, value = 20, bind = myVelocity)
velocityText = wtext(text = velocitySlider.value)

car = box(pos = vec(0,0,0), size = vec(2,1,1), v = vec(20,0,0), color = color.red)
person = sphere(pos = vec(40,0,0), radius = 0.5, color = color.blue)
crashLabel = label(text = "Crash", box = False, color = color.yellow, visible = False)

g = 9.8
mu = 0.8

t = 0
dt = 0.01

while True:
    rate(1/dt)

    if btnDraw.disabled == True:
        if mag(car.pos) > 20:
            a = -g*mu*norm(car.v)
            car.v += a*dt
        car.pos += car.v*dt
        if mag(car.v) < 0.05 or mag(car.pos - person.pos) < 1.5:
            if mag(car.pos - person.pos) < 1.5:
                crashLabel.visible = True
            car.v = vec(0,0,0)
            scene.waitfor('click')
            crashLabel.visible = False
            btnDraw.disabled = False
            car.pos = vec(0,0,0)
            t = 0

    t += dt
