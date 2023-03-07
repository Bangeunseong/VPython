from vpython import *

scale_capacity = 5.0

r = 384400000
G = 6.67e-11

earth = sphere(pos = vec(0,0,0), radius = scale_capacity * 6371000, texture = textures.earth)
moon = sphere(pos = vec(r,0,0), radius = scale_capacity * 1373000, color = color.white)