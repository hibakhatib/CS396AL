import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)

p.stepSimulation()
t.sleep(60)
print("hello")

p.disconnect()