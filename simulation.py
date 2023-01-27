import pybullet as p
from world import WORLD
from robot import ROBOT 
import time as t
import pybullet_data
import numpy as numpy
import constants as c
import time as time



class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        
    
    def Run(self):
        for i in range(1000):
            p.stepSimulation() 
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(1/60)  
            
     
    def __del__(self):
        p.disconnect()
        
        
        
        



















# class SIMULATION:
#     def __init__(self):
#         self.world = WORLD()
#         self.robot = ROBOT()
#         self.robot.robotId()
        
#     def RUN():
#         bamplitude = -numpy.pi/4
#         bfrequency = 10
#         bphaseOffset = 0
#         famplitude = numpy.pi/4
#         ffrequency = 15
#         fphaseOffset = 0
#         f = numpy.linspace(0, 2*numpy.pi, 1000)
#         b = numpy.linspace(0, 2*numpy.pi, 1000)
#         backLegSensorValues = numpy.zeros(1000)
#         frontLegSensorValues = numpy.zeros(1000)
#         for i in range(1000):
#             backLegSensorValues[i] = numpy.sin(b[i]) * numpy.pi/4
#             backLegSensorValues[i] = bamplitude * numpy.sin(bfrequency * (b[i] + bphaseOffset))
#         for i in range(1000):
#             frontLegSensorValues[i] = numpy.sin(f[i]) * numpy.pi/4
#             frontLegSensorValues[i] = famplitude * numpy.sin(ffrequency * (f[i] + fphaseOffset))
#         for i in range(1000):
#             p.stepSimulation()
#             backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
#             frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
#             print(backLegSensorValues[i], frontLegSensorValues[i])
#             pyrosim.Set_Motor_For_Joint( 
#                                 bodyIndex = robotId,
#                                 jointName = "Torso_Backleg",
#                                 controlMode = p.POSITION_CONTROL,
#                                 targetPosition = backLegSensorValues[i],
#                                 maxForce = 300
#                                 )
#             pyrosim.Set_Motor_For_Joint( 
#                                 bodyIndex = robotId,
#                                 jointName = "Torso_Frontleg",
#                                 controlMode = p.POSITION_CONTROL,
#                                 targetPosition = frontLegSensorValues[i],
#                                 maxForce = 300
#                                 )
#             t.sleep(1/30)
        
        
#     def __del__(self):
#         p.disconnect()
        
#     physicsClient = p.connect(p.GUI)    
#     p.setAdditionalSearchPath(pybullet_data.getDataPath())
#     p.setGravity(0,0,-100) 
#     pyrosim.Prepare_To_Simulate()
