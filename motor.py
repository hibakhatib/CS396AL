import pyrosim.pyrosim as pyrosim 
import pybullet as p 
import constants as c 
import numpy as numpy 

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
    
    
    # def Prepare_To_Act(self):
    #     self.amplitude = c.bamplitude;
    #     self.frequency = c.bfrequency;
    #     self.offset = c.bphaseOffset;
    #     self.motorValues = numpy.zeros(1000)
        
    #     #self.motorValues[i] = self.amplitude * numpy.sin((self.frequency/2) * (c.b[i] + self.offset))
    #     x = numpy.linspace(-numpy.pi, numpy.pi, 1000)
    #     if self.jointName == "Torso_Backleg":
    #         self.motorValues = self.amplitude * numpy.sin(self.frequency * (x + self.offset))
            #c.backLegSensorValues[i] = numpy.sin(c.b[i]) * numpy.pi/2
                    
            
        #for i in range(1000):
            #c.frontLegSensorValues[i] = numpy.sin(c.f[i]) * numpy.pi/4

    # def Set_Value(self, robotId, desiredAngle):
    #     pyrosim.Set_Motor_For_Joint( 
    #                             bodyIndex = robotId,
    #                             jointName = self.jointName,
    #                             controlMode = p.POSITION_CONTROL,
    #                             targetPosition = self.motorValues[desiredAngle],
    #                             maxForce = 50
    #                             )
        