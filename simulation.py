import pybullet as p
import time as time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("simple.urdf")
p.setGravity(0,0,-100) 
p.loadSDF("world.sdf")


backLegSensorValues = numpy.zeros(10000)
pyrosim.Prepare_To_Simulate(robotId)
for i in range(1001):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    print(backLegSensorValues)  
    time.sleep(1/30)

numpy.save('sensorvalues', backLegSensorValues)



p.disconnect()