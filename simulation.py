import pybullet as p
import time as time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random as random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("simple.urdf")
p.setGravity(0,0,-100) 
p.loadSDF("world.sdf")



pyrosim.Prepare_To_Simulate(robotId)


bamplitude = -numpy.pi/4
bfrequency = 10
bphaseOffset = 0

famplitude = numpy.pi/4
ffrequency = 15
fphaseOffset = 0

#x = numpy.linspace(numpy.pi, -numpy.pi, 1000)
#targetAngles = numpy.sin(x)
#numpy.save('targetAngles2', targetAngles)


f = numpy.linspace(0, 2*numpy.pi, 1000)
b = numpy.linspace(0, 2*numpy.pi, 1000)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)


for i in range(1000):
    backLegSensorValues[i] = numpy.sin(b[i]) * numpy.pi/4
    backLegSensorValues[i] = bamplitude * numpy.sin(bfrequency * (b[i] + bphaseOffset))
    
for i in range(1000):
    frontLegSensorValues[i] = numpy.sin(f[i]) * numpy.pi/4
    frontLegSensorValues[i] = famplitude * numpy.sin(ffrequency * (f[i] + fphaseOffset))
    

#for i,k in enumerate(numpy.linspace(0, 2*numpy.pi, 1000)):
 #   frontLegSensorValues[i] = famplitude * numpy.sin(ffrequency*i + fphaseOffset)
 #   backLegSensorValues[i] = bamplitude * numpy.sin(bfrequency*i + bphaseOffset)


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    print(backLegSensorValues[i], frontLegSensorValues[i])
    pyrosim.Set_Motor_For_Joint( 
                                bodyIndex = robotId,
                                jointName = "Torso_Backleg",
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = backLegSensorValues[i],
                                maxForce = 300
                                )
    pyrosim.Set_Motor_For_Joint( 
                                bodyIndex = robotId,
                                jointName = "Torso_Frontleg",
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = frontLegSensorValues[i],
                                maxForce = 300
                                )
                                
    time.sleep(1/30)

#numpy.save('backLegSensorValues', backLegSensorValues)
#numpy.save('frontLegSensorValues', frontLegSensorValues)



p.disconnect()