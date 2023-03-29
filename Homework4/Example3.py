from vpython import *

#**Number1**
# What's the position of elevator after 10 sec passed?
# -> 4m above the ground(offset)

#**Number2**
# Get sectors when elevator users felt less force than gravity!
# -> 5~6sec, 7~8sec

#**Number3**

t = 0
dt = 0.001

elevator = box(pos = vec(0,0,0), size = vec(2,4,2), color = color.red)
ground = box(pos = vec(0,-2.05,0), size = vec(4,0.1,4), color = color.white)

elevator.a = vec(0,2,0)
elevator.v = vec(0,0,0)

motion_graph = graph(title = 'position-time', xtitle = 't', ytitle = 'y')
g_elevator = gcurve(graph = motion_graph, color = color.green)
velocity_graph = graph(title = "velovity-time", xtitle = 't', ytitle = 'v')
g_elevator_v = gcurve(graph = velocity_graph, color = color.cyan)

while t <= 10:
    rate(1/dt)
    if t > 1 and t <= 2:
        elevator.v += elevator.a*dt
    elif t > 5 and t <= 6:
        elevator.v -= elevator.a*dt
    elif t > 7 and t <= 8:
        elevator.v -= elevator.a*dt
    elif t > 9 and t <= 10:
        elevator.v += elevator.a*dt
    elevator.pos += elevator.v*dt
    g_elevator.plot(pos = (t,elevator.pos.y))
    g_elevator_v.plot(pos = (t,elevator.v.y))
    t += dt
print(elevator.pos)