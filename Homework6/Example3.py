from vpython import *

t = 0
dt = 24*3600
G = 6.67e-11

mercury = sphere(pos = vec(5.8e10, 0, 0), radius = 2.4e9, mass = 3.30e23, v = vec(0, 47360, 0), color = color.white)
venus = sphere(pos = vec(-1.1e11, 0, 0), radius = 6e9, mass = 4.87e24, v = vec(0, -35020, 0), color = color.orange)
earth = sphere(pos = vec(0, 1.5e11, 0), radius = 6.4e9, mass = 5.97e24, v = vec(-29783, 0, 0), texture = textures.earth)
sun = sphere(pos = vec(0, 0, 0), radius = 3.5e10, mass = 1.99e30, v = vec(0, 0, 0), color = color.red)

attach_trail(mercury, radius = mercury.radius/2, color = color.white)
attach_trail(venus, radius = venus.radius/2, color = color.orange)
attach_trail(earth, radius = earth.radius/2, color = color.white)

while True:
    rate(100)
    mercury.force = -G*sun.mass*mercury.mass/mag(sun.pos - mercury.pos)**2*norm(mercury.pos - sun.pos) - G*mercury.mass*venus.mass/mag(venus.pos - mercury.pos)**2*norm(mercury.pos - venus.pos) - G*mercury.mass*earth.mass/mag(mercury.pos - earth.pos)**2*norm(mercury.pos - earth.pos)
    venus.force = -G*sun.mass*venus.mass/mag(venus.pos - sun.pos)**2*norm(venus.pos - sun.pos) - G*mercury.mass*venus.mass/mag(venus.pos - mercury.pos)**2*norm(venus.pos - mercury.pos) - G*earth.mass*venus.mass/mag(earth.pos - venus.pos)**2*norm(venus.pos - earth.pos)
    earth.force = -G*sun.mass*earth.mass/mag(earth.pos - sun.pos)**2*norm(earth.pos - sun.pos) - G*venus.mass*earth.mass/mag(venus.pos - earth.pos)**2*norm(earth.pos - venus.pos) - G*mercury.mass*earth.mass/mag(mercury.pos - earth.pos)**2*norm(earth.pos - mercury.pos)
    sun.force = G*sun.mass*mercury.mass/mag(sun.pos - mercury.pos)**2*norm(mercury.pos - sun.pos) + G*sun.mass*venus.mass/mag(venus.pos - sun.pos)**2*norm(venus.pos - sun.pos) + G*sun.mass*earth.mass/mag(earth.pos - sun.pos)**2*norm(earth.pos - sun.pos)

    mercury.v += mercury.force/mercury.mass*dt
    venus.v += venus.force/venus.mass*dt
    earth.v += earth.force/earth.mass*dt
    sun.v += sun.force/sun.mass*dt

    mercury.pos += mercury.v*dt
    venus.pos += venus.v*dt
    earth.pos += earth.v*dt
    sun.pos += sun.v*dt

    t += dt