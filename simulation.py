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
frontLegSensorValues = numpy.zeros(1000)
pyrosim.Prepare_To_Simulate(robotId)
for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    print(backLegSensorValues)  
    time.sleep(1/30)

numpy.save('backLegSensorValues', backLegSensorValues)
numpy.save('frontLegSensorValues', frontLegSensorValues)



p.disconnect()