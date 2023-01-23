import numpy as numpy 
import pyrosim.pyrosim as pyrosim 

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)
        #self.sensorValues = pyrosim.Get_Touch_Sensor_Value_For_Link(linkName)
        
    # def Save_Values(self,filename, x):
    #     numpy.save(filename, x)
    #numpy.save("data/"+str(self.linkName)+".npy", self.values)
        
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
        
        
