from vpython import *

tanklowerbody = box(pos=vec(0,0,0), size=vec(1.6,0.4,1), color=vec(0.2,0.6,0.2))
tankupperbody = box(pos=tanklowerbody.pos + vec(0,0.32,0), size=vec(1,0.24,0.6), color=vec(0.2,0.6,0.2))
tankcannon = box(pos=tankupperbody.pos + vec(0.4,0,0), size=vec(1.2,0.1,0.1), color=vec(0.2,0.6,0.2))

scene.center = tankupperbody.pos
scene.camera.pos = tankupperbody.pos + vec(0,0.5,0)
scene.camera.axis = vec(0.7,-0.3,0)

mouse_pos = scene.mouse.pos
scene.camera.rotate(angle=radians(45), axis=vec(0,1,0), origin=tankupperbody.pos)
tankupperbody.rotate(angle=radians(45), axis=vec(0,1,0))
tankcannon.rotate(angle=radians(45), axis=vec(0,1,0), origin=tanklowerbody.pos)