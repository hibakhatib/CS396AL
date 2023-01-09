import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

p.stepSimulation()

t.sleep(60)
    
 
p.disconnect()