import numpy as numpy 

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)
        
    def Save_Values(filename, x):
        numpy.save(filename, x)
        
        
