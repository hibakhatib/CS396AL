import pybullet as p 
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK


from sensor import SENSOR
from motor import MOTOR 



class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("simple.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
       
        
    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,i):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(i)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def Act(self,i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                
    def Think(self):
        self.nn.Update()
        #self.nn.Print()
        
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("fitness.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()

            
        
        
        
