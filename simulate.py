# import pybullet as p
# import time as time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy as numpy
# import random as random
# import constants as c

from simulation import SIMULATION


#see step 53
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

simulation = SIMULATION()
simulation.Run()


# robotId = p.loadURDF("simple.urdf")
# planeId = p.loadURDF("plane.urdf")

# p.setGravity(0,0,-10) 
# p.loadSDF("world.sdf")

# #x = numpy.linspace(numpy.pi, -numpy.pi, 1000)
# #targetAngles = numpy.sin(x)
# #numpy.save('targetAngles2', targetAngles)
# targetAngles = numpy.load("data/targetAngles.npy")
# targetAngles2 = numpy.load("data/targetAngles2.npy")
# targetAnglesbest = numpy.load("targetAngles2.npy")
# sensorvals =  numpy.load("data/sensorvalues.npy")



# pyrosim.Prepare_To_Simulate(robotId)


# for i in range(1000):
#     c.backLegSensorValues[i] = numpy.sin(c.b[i]) * numpy.pi/2
#     c.backLegSensorValues[i] = c.bamplitude * numpy.sin(c.bfrequency * (c.b[i] + c.bphaseOffset))
    
# for i in range(1000):
#     c.frontLegSensorValues[i] = numpy.sin(c.f[i]) * numpy.pi/4
#     c.frontLegSensorValues[i] = c.famplitude * numpy.sin(c.ffrequency * (c.f[i] + c.fphaseOffset))
    


# for i in range(1000):
#     p.stepSimulation()
#     c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
#     c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
#     print(c.backLegSensorValues[i], c.frontLegSensorValues[i])
#     pyrosim.Set_Motor_For_Joint( 
#                                 bodyIndex = robotId,
#                                 jointName = "Torso_Backleg",
#                                 controlMode = p.POSITION_CONTROL,
#                                 targetPosition = targetAnglesbest[i],
#                                 maxForce = 100
#                                 )
#     pyrosim.Set_Motor_For_Joint( 
#                                 bodyIndex = robotId,
#                                 jointName = "Torso_Frontleg",
#                                 controlMode = p.POSITION_CONTROL,
#                                 targetPosition = sensorvals[i],
#                                 maxForce = 100
#                                 )
                                
#     time.sleep(1/60)

# p.disconnect()













# #for i,k in enumerate(numpy.linspace(0, 2*numpy.pi, 1000)):
#  #   frontLegSensorValues[i] = famplitude * numpy.sin(ffrequency*i + fphaseOffset)
#  #   backLegSensorValues[i] = bamplitude * numpy.sin(bfrequency*i + bphaseOffset)

