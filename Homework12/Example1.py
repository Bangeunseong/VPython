from vpython import *

s_white = sphere(pos = vec(0,0,0), radius = 0.05, mass = 1, v = vec(0.3,0,0), color = color.white, make_trail = True)
s_red = sphere(pos = vec(1,0.05,0), radius = 0.05, mass = 1, v = vec(0,0,0), color = color.red)
s_green = sphere(pos = vec(1.5,0.4,0), radius = 0.05, mass = 1, v = vec(0,0,0), color = color.green)

e = 1.0
total_energy = 0.5*s_white.mass*mag(s_white.v)**2
t = 0
dt = 0.01

v_com_xy = graph(title="V_Com_x", xtitle="t", ytitle="x, y")
v_graph_x = gcurve(color = color.red, graph = v_com_xy)
v_graph_y = gcurve(color = color.blue, graph = v_com_xy)

def collision(b1, b2, e):
    c = b2.pos - b1.pos
    c_hat = norm(c)
    dist = mag(c)

    if dot(b1.v-b2.v, c_hat) < 0:
        return False
    
    v1_c = dot(b1.v, c_hat)*c_hat
    v1_p = b1.v - v1_c
    v2_c = dot(b2.v, c_hat)*c_hat
    v2_p = b2.v - v2_c
    total_mass = b1.mass + b2.mass

    if dist < b1.radius + b2.radius:
        v1 = ((b1.mass - e*b2.mass)*v1_c + (1+e)*b2.mass*v2_c)/total_mass
        v2 = ((b2.mass - e*b1.mass)*v2_c + (1+e)*b1.mass*v1_c)/total_mass
        b1.v = v1 + v1_p
        b2.v = v2 + v2_p
        return True
    else:
        return False
    
while True:
    rate(1/dt)
    total_v = s_white.v + s_red.v + s_green.v
    v_graph_x.plot(pos = (t, total_v.x))
    v_graph_y.plot(pos = (t, total_v.y))

    collision(s_white, s_red, e)
    collision(s_red, s_green, e)
    collision(s_white, s_green, e)

    s_white.pos += s_white.v*dt
    s_red.pos += s_red.v*dt
    s_green.pos += s_green.v*dt

    t += dt
