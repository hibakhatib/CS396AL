import numpy as numpy 
import random

bamplitude = -numpy.pi/2
bfrequency = 10
bphaseOffset = 0

population = 1

famplitude = numpy.pi/2
ffrequency = 5
fphaseOffset = 0

length = 1
width = 1
height = 1

numLinks = random.randint(3, 10)
numJoints = numLinks -1

snake_length = random.randint(1, 10)
numSensorNeurons = random.randint(1, 10)
numMotorNeurons = snake_length
sensors = []
for i in range(numSensorNeurons):
    r = random.randint(0, snake_length + 1)
    sensors.append(r)


f = numpy.linspace(0, 2*numpy.pi, 1000)
b = numpy.linspace(0, 2*numpy.pi, 1000)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

numberOfGenerations = 1

numSensorNeurons = 6
numMotorNeurons = 12

motorJointRange = 0.2
