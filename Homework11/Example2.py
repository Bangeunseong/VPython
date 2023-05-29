from vpython import *

Earth = sphere(pos = vec(0,0,0), radius = 6400000, mass = 5.972e24, texture = textures.earth)
spaceship = sphere(pos = vec(Earth.radius,0,0), radius = 5, mass = 15000, make_trail = True)

G = 6.673e-11

#vi = sqrt(Earth.mass*G/Earth.radius)
#vi = sqrt(1.5*Earth.mass*G/Earth.radius)
vi = sqrt(2*Earth.mass*G/Earth.radius)

#spaceship.v = vec(vi,0,0)
spaceship.v = vi*norm(vec(1,1,0))

v_graph = gcurve(color = color.cyan)

t = 0
dt = 60

while True:
    rate(100)
    if mag(spaceship.pos - Earth.pos) < Earth.radius:
        break

    r = spaceship.pos - Earth.pos
    spaceship.f = -G*Earth.mass*spaceship.mass/mag(r)**2*norm(r)
    spaceship.v += spaceship.f/spaceship.mass*dt
    spaceship.pos += spaceship.v*dt

    v_graph.plot(t/3600, mag(spaceship.v))

    t += dt