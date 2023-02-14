import pybullet as p 
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR 
import os
import numpy



class ROBOT:
    def __init__(self, solutionID):
        self.motors = {}
        self.sensors = {}
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        os.system("del brain" + str(self.solutionID) + ".nndf")
        
        
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
       
        
    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,i):
        i = 0
        c = 0
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(i)
            if c == 2:
                self.sensors[linkName].Set_Value(i, numpy.sin(2*i))
            i+=1
            
        
        # for sensor in self.sensors:
        #     self.sensors[sensor].Get_Value(i)

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
        #zCoordinateOfLinkZero = positionOfLinkZero[2]
        
        #basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        #basePosition = basePositionAndOrientation[0]
        #xCoordinateOfLinkZero = basePosition[0]

        
        f = open("fitness" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        #os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
        
        
        # f = open("brain" + str(self.solutionID) + ".nndf", "w")
        # f.write(str())
        #os.system("mv temp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")
        # f = open("fitness.txt", "w")
        # f.write(str(xCoordinateOfLinkZero))
        # f.close()




        # for file in os.listdir(r"C:\Users\hibar\CS396AL2"):
        #     if file.startswith("brain"):
        #         os.system("rm brain*.nndf")
            
        
        
        
