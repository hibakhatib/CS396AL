import pybullet as p 
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR 
import os
import numpy
import constants as c



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
        # i = 0
        # c = 0
        # for linkName in pyrosim.linkNamesToIndices:
        #     self.sensors[linkName].Get_Value(i)
        #     if c == 2:
        #         self.sensors[linkName].Set_Value(i, numpy.sin(2*i))
        #     i+=1
            
        
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(i)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            # print(MOTOR(jointName))
            # print(self.motors.values)
            self.motors[jointName] = MOTOR(jointName)
            # print((self.motors[jointName]))

            
    def Act(self,i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) 
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                
    def Think(self):
        self.nn.Update()
        #self.nn.Print()
        
    def Get_Fitness(self, solutionID):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        
        f = open("fitness" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        
    def Get_MotorValues(self, solutionID):
        for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    motorVals = str(self.nn.neurons[neuronName].Print())
                    if None in motorVals:
                        motorVals.replace('None', '')
                    motorVals = motorVals.strip()
                    print(motorVals)
                    breakpoint()
                    f = open("motor" + str(self.solutionID) + ".txt", "w")
                    f.write(motorVals)
                    f.close()
                    
    def Get_NumLinks(self, solutuionID):
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)
            print(c.limbs)   
            breakpoint()     
            
        
        
        
