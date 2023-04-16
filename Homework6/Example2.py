from vpython import *

#1
G = 6.67e-11
earth_radius = 6400000
earth_mass = 5.9736*10**24

planet_radius = 3
planet_mass = (earth_mass/(earth_radius**2))*planet_radius**2

print("Mass of the planet:", planet_mass, "kg")

#2
#Comment : 머리와 발에 작용하는 중력가속도의 차이는 약 4.3 정도로 무시할만한 값이 아니다
#이렇게 큰 차이가 나는 이유는 어린왕자 별의 반지름이 겨우 3m라서 키가 1m라도 큰 차이가 발생하는 것이다

G_Head = -G*planet_mass/(planet_radius+1)**2
G_Foot = -G*planet_mass/planet_radius**2
print("Gravitational acceleration differenct:", G_Head - G_Foot, "m/s^2")

#3
#Comment : 어린왕자의 velocity는 등속원운동을 한다는 조건 하에
#구심가속도를 구하는 식으로 구할 수 있다.
#a = v^2/R 

t = 0
dt = 0.001

planet = sphere(pos = vec(0, 0, 0,), radius = planet_radius, mass = planet_mass, v = vec(0, 0, 0), color = color.white)
prince = sphere(pos = vec(0, planet.radius + 1, 0), radius = 0.1, mass = 1, v = vec(sqrt(-G_Head*(planet_radius + 1)), 0, 0) , color = color.white)

print("Velocity:", sqrt(-G_Head*(planet_radius + 1)), "m/s^2")

while True:
    rate(1/dt)
    F = -G*planet.mass*prince.mass/mag(planet.pos - prince.pos)**2*norm(planet.pos - prince.pos)
    planet.force = F
    prince.force = -F

    planet.v += planet.force/planet.mass*dt
    prince.v += prince.force/prince.mass*dt
    planet.pos += planet.v*dt
    prince.pos += prince.v*dt

    t += dt
