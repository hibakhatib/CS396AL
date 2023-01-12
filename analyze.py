import numpy as numpy 
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')

print(backLegSensorValues)

b, = plt.plot(backLegSensorValues, label = "backLeg")

frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
f, = plt.plot(frontLegSensorValues, label = "frontLeg")
plt.legend()
plt.xlim(0, 500)
plt.show()
