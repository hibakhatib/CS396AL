import numpy as numpy 

bamplitude = -numpy.pi/2
bfrequency = 10
bphaseOffset = 0

population = 5

famplitude = numpy.pi/2
ffrequency = 5
fphaseOffset = 0

length = 1
width = 1
height = 1


f = numpy.linspace(0, 2*numpy.pi, 1000)
b = numpy.linspace(0, 2*numpy.pi, 1000)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

numberOfGenerations = 1

numSensorNeurons = 9
numMotorNeurons = 8

motorJointRange = 0.2
