import pybullet as p
import time as time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#robot2Id = p.loadURDF("r.urdf")
simpleId = p.loadURDF("simple.urdf")
p.setGravity(0,0,-100) 
p.loadSDF("world.sdf")


for i in range(1001):
    p.stepSimulation()
    time.sleep(1/30)



p.disconnect()