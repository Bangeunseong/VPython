from vpython import *

#Arrow Object
r = vector(3,4,5)
A = arrow(pos = vec(0,0,0), axis = r, shaftwidth = 0.2)

#----------------------Conditions
a = vector(1,2,3)
b = vector(-4,5,6)

#Summation of vector
c = a + b 

#Subtraction of vector
d = a - b

#Vector * Scalar
e = a*4

#Unit vector **All same**
I = hat(a)
I = a.hat
I = norm(a)

#Magnitude of vector
a_mag = mag(a)

#Math Funtions
radian = radians(45)#Get radian value from degree
degree = degrees(radian)#Get degree value from radian
r_sin = sin(radian) #Get sin value
r_cos = cos(radian) #Get cos value
r_tan = tan(radian) #Get tan calue

radian = abs(radian) #Get Absolute value
radian = sqrt(radian)#Get Square root value
radian = exp(radian) #Get exponent value
radian = log(radian) #Get log value
radian = pow(radian,10) #Get exponent value
radian = pi

ab_dot = dot(a,b) #Get a dot b
ab_dot = a.dot(b) #Same

radian = diff_angle(a,b) #Get angle difference between a and b
radian = a.diff_angle(b) #Same

ab_cross = cross(a,b) #Get a X b **Beware of positions of vector**
ab_cross = a.cross(b) #Same      cross(a,b) != cross(b,a)

#Dismantle vector
rhat = hat(a) #Unit vector of a
v_para = dot(a,rhat)*rhat #Parallel Vector
v_perp = a - v_para #Horizontal vector

#---------------------------------
#-------------------------Practice

t = 15
x = -0.31*t**2 + 7.2*t + 28
y = 0.22*t**2 - 9.1*t + 30

v_x = -0.62*t + 7.2
v_y = 0.44*t - 9.1

acc_x = -0.62
acc_y = 0.44

#Pos Vector
pos_v = vec(x,y,0)
print(pos_v)

#Velocity Vector
Velocity_v = vec(v_x,v_y,0)
print(Velocity_v)

#Acceleration Vector
acc_v = vec(acc_x,acc_y,0)
print(acc_v)

