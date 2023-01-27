import pyrosim.pyrosim as pyrosim 
import pybullet as p 
import constants as c 
import numpy as numpy 

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = {}
        self.Prepare_To_Act()
    
    def Prepare_To_Act(self):
        self.amplitude = c.bamplitude;
        self.frequency = c.bfrequency;
        self.offset = c.bphaseOffset;
        for i in range(1000):
            if self.jointName == "Torso_Backleg":
                self.motorValues[i] = self.amplitude * numpy.sin((self.frequency/2) * (c.b[i] + self.offset))
        for j in range(1000):
            if self.jointName == "Torso_Frontleg":
                self.motorValues[j] = self.amplitude * numpy.sin(self.frequency * (c.f[j] + self.offset))
            
    def Set_Value(self, robotId, i):
        pyrosim.Set_Motor_For_Joint( 
                                bodyIndex = robotId,
                                jointName = self.jointName,
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = self.motorValues[i],
                                maxForce = 50
                                )
        
        


#under prepare to act

            #c.backLegSensorValues[i] = numpy.sin(c.b[i]) * numpy.pi/2
                    
            
        #for i in range(1000):
            #c.frontLegSensorValues[i] = numpy.sin(c.f[i]) * numpy.pi/4
