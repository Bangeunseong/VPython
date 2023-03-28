from vpython import *

rf = vector(3,3.5,0)#last pos
ri = vector(2,4,0)  #first pos
dr = rf - ri        #difference of pos

tf = 15.1           #last time
ti = 15.0           #first time
dt = tf - ti        #difference of time
vavg = dr/dt

print(rf,"-",ri,"=",dr)
print("v_avg =",vavg,"speed =",mag(vavg))
print("v_hat =",hat(vavg))
print(mag(vavg)*hat(vavg))

x_axis = arrow(axis = vector(7,0,0),shaftwidth = 0.1)
y_axis = arrow(axis = vector(0,7,0),shaftwidth = 0.1)

sphere(radius = 0.1, pos = ri)
sphere(radius = 0.1, pos = rf)
sf = 1.0/3.0

ri_vec = arrow(axis = ri, shaftwidth = 0.2, color = color.yellow)
rf_vec = arrow(axis = rf, shaftwidth = 0.2, color = color.yellow)
dr_vec = arrow(pos = ri, axis = dr, shaftwidth = 0.2, color = color.blue)
vavg_vec = arrow(pos = ri, axis = vavg*sf, shaftwidth = 0.1, color = color.green)