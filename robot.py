import pybullet as p
import pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR 


class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("simple.urdf")
        #pyrosim.Prepare_To_Simulate(self.robotId)
        
    def Prepare_to_sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,i):
        self.sensors = {}
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(i)
        # for t in range(1000):
        #     if t == i:
        #         SENSOR.Get_value(i)
        #     t = t + 1
            
    def Get_Value(self, i):
        self.values = {}
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
    def Prepare_To_Act(self):
        self.joints = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.sensors[jointName] = SENSOR(jointName)
            
    def Act(self,i):
        self.motors = {}
        for motor in self.motors:
            self.motors[motor].Set_Value(self.robotId, i)
            
        
        
        
