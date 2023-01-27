import numpy as numpy 
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)
        
    def Save_Values(self):
        numpy.save("data/"+str(self.linkName)+".npy", self.values)
        
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
    
