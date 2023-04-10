from vpython import *

R = 1
w = 2
t = 0
dt = 0.001

r = vec(R*cos(w*t),R*sin(w*t), 0)
v = vec((-R)*w*sin(w*t), R*w*cos(w*t), 0)
a = vec((-R)*(w**2)*cos(w*t), (-R)*(w**2)*sin(w*t), 0)

r_arrow = arrow(axis = r, color = color.green, shaftwidth = 0.02)
v_arrow = arrow(axis = v, color = color.blue, shaftwidth = 0.02)
a_arrow = arrow(axis = a, color = color.red, shaftwidth = 0.02)

while t < 5:
    rate(1/dt)
    r_arrow.axis.x = R*cos(w*t)
    r_arrow.axis.y = R*sin(w*t)
    v_arrow.axis.x = (-R)*w*sin(w*t)
    v_arrow.axis.y = R*w*cos(w*t)
    a_arrow.axis.x = (-R)*(w**2)*cos(w*t)
    a_arrow.axis.y = (-R)*(w**2)*sin(w*t)
    t += dt
print("theta :", degrees(acos(dot(v,a)/(mag(a)*mag(v)))))