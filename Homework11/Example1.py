from vpython import *

Earth = sphere(pos = vec(0,0,0), radius = 6400000, mass = 5.972e24, texture = textures.earth)
Moon = sphere(pos = vec(384400000,0,0), radius = 1738000, mass = 7.36e22, color = color.white)

attach_trail(Moon, radius = Moon.radius/3, color = color.white)

G = 6.673e-11
vi = sqrt(G*Earth.mass/mag(Earth.pos - Moon.pos)**1)
Moon.v = vec(0,vi*0.7,0)
#Moon.v = sqrt(2)*vec(0,vi,0)
#Moon.v = sqrt(3)*vec(0,vi,0)
Earth.v = -Moon.v*Moon.mass/Earth.mass

k_graph = gcurve(color = color.cyan)
u_graph = gcurve(color = color.green)
ku_graph = gcurve(color = color.black)

t = 0
dt = 3600

while t < 10*365*24*69*60:
    rate(100)
    r = Moon.pos - Earth.pos
    
    Moon.f = -G*Earth.mass*Moon.mass/mag(r)**2*norm(r)
    Earth.f = -Moon.f

    Moon.v += Moon.f/Moon.mass*dt
    #Earth.v += Earth.f/Earth.mass*dt
    
    Moon.pos += Moon.v*dt
    #Earth.pos += Earth.v*dt

    k = 0.5*Moon.mass*mag(Moon.v)**2
    u = -G*Earth.mass*Moon.mass/mag(Moon.pos)

    k_graph.plot(t/60/60/24, k)
    u_graph.plot(t/60/60/24, u)
    ku_graph.plot(t/60/60/24, k + u)

    if mag(r) < Earth.radius + Moon.radius:
        print(t/60/60/24)
        break
    t += dt
