from vpython import *

watertank = box(pos = vec(0,0,0), size = vec(5, 5, 5), color = color.blue, opacity = 0.5)
rock = sphere(pos = vec(-2.5+0.05,0,0), radius = 0.05, v = vec(30,0,0), color = color.red)

g = vec(0,-9.8,0)

watertank.rho = 1000
rock.rho = 2500

rock.volume = 4/3*pi*rock.radius**3
rock.surface = pi*rock.radius**2
rock.m = rock.volume*rock.rho

Cd = 0.5

t = 0
dt = 0.01

motiongraph = graph(title='X_Position, Time', xtitle='t', ytitle='x')
rock_position = gcurve(color = color.red, graph = motiongraph)

while rock.pos.y >= -2.5 + 0.05:
    rate(1/dt)
    rock_position.plot(pos = (t, rock.pos.x + 2.5 - 0.05))
    rock.F = (rock.volume*(rock.rho - watertank.rho)*g) + ((-1/2)*Cd*watertank.rho*rock.surface*mag(rock.v)**2*norm(rock.v))
    rock.v += rock.F/rock.m*dt
    rock.pos += rock.v*dt
    t += dt
print("X_Difference :", rock.pos.x)
print("Time :", t)