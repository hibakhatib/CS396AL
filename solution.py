import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random 
import time



class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(3,2) * 2 - 1
        #self.weights = (self.weights * 2) -1
        # self.fitness = 0
        self.myID = nextAvailableID
        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python simulate.py " + directOrGUI + " " + str(self.myID) + " &")
        
    def Wait_For_Simulation_To_End(self):
        fitFile = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitFile):
            time.sleep(1/100)
        
        fitnessFile = open(fitFile, "r")
        fit = fitnessFile.read()
        self.fitness = float(fit)
        fitnessFile.close()
        os.system("del " + fitFile)
        
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,-2,0.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("simple.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[1,1,1])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.End()

    def Create_Brain(self):
            pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
            pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
            pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
            pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
            pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
            pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
            pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1)
            pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1)
            pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 1)
            pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1 )
            pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 1 )
            pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1 )
            for currentRow in range(3):
                for currentCol in range(2):
                    pyrosim.Send_Synapse(sourceNeuronName= currentRow, 
                                             targetNeuronName= currentCol+3, 
                                             weight = self.weights[currentRow][currentCol])
                    #print(self.weights[currentRow][currentCol])
            pyrosim.End()
            
    def Mutate(self):
        row = random.randint(0,2)
        col = random.randint(0,1)
        self.weights[row, col] = random.random() * 2 -1
    
    def Set_ID(self, id):
        self.myID = id
        
        
        