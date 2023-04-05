from vpython import *

def biInterp(pos, dx, dy, grid):
    cellx = int(pos.x/dx)
    celly = int(pos.y/dy)

    cellbox = box(pos = vec((cellx + 0.5)*dx, (celly+0.5)*dy, -0.1), length = dx, height = dy, width = 0.05)
    
    rx = pos.x - cellx*dx
    ry = pos.y - celly*dy
    resultx0 = grid[cellx][celly]*(dx - rx)/dx + grid[cellx + 1][celly]*rx/dx
    resultx1 = grid[cellx][celly + 1]*(dx - rx)/dx + grid[cellx + 1][celly + 1]*rx/dx
    result = resultx0*(dy-ry)/dy + resultx1*ry/dy
    
    return result

n = 20
m = 20
dx = 1
dy = 1

scene.center = vec(n*dx/2,m*dy/2,0)

rList = []
objList = []

for i in range(0,n):
    rList.append([])
    objList.append([])
    for j in range(0,m):
        rList[i].append(vec(random(),random(),0))
        objList[i].append(arrow(pos = vec(i*dx,j*dy,0),axis = rList[i][j], shaftwidth = 0.2))

r_i = vec(random(), random(), 0)

ball = sphere(pos = r_i, radius = 0.2, color = color.yellow, make_trail = True)
ball.v = vec(0,0,0)
attach_arrow(ball,"v")
attach_trail(ball, color = color.red)

t = 0
dt = 0.1
while ball.pos.x < (n - 1)*dx and ball.pos.y < (m - 1)*dy:
    rate(100)
    ball.v = biInterp(ball.pos,dx,dy,rList)
    ball.pos += ball.v*dt
    t += dt
print("loop out")
