import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random 
import time
import constants as c



class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
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
        pyrosim.Send_Cube(name="Box", pos=[-2,-2,0.5] , size=[c.length, c.width, c.height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("simple.urdf")
        
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[c.length, c.width, c.height])
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        
        pyrosim.Send_Cube(name = "LeftLeg", pos = [-0.5,0,0], size = [1, 0.2, 0.2])
        pyrosim.Send_Cube(name = "RightLeg", pos = [0.5,0,0], size = [1, 0.2, 0.2])
        pyrosim.Send_Joint(name = "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [.5,0,1], jointAxis = "0 1 0")
        
        pyrosim.Send_Cube(name = "BackLowerLeg", pos = [0,0,-0.5], size = [0.2, 0.2, 1])
        pyrosim.Send_Cube(name = "FrontLowerLeg", pos = [0,0,-0.5], size = [0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg", parent = "FrontLeg", child = "FrontLowerLeg", type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg", parent = "BackLeg", child = "BackLowerLeg", type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        
        pyrosim.Send_Cube(name = "LeftLowerLeg", pos = [0,0,-0.5], size = [0.2, 0.2,1])
        pyrosim.Send_Cube(name = "RightLowerLeg", pos = [0,0,-0.5], size = [0.2, 0.2,1])
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg", parent = "LeftLeg", child = "LeftLowerLeg", type = "revolute", position = [-1, 0,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg", parent = "RightLeg", child = "RightLowerLeg", type = "revolute", position = [1, 0,0], jointAxis = "0 1 0")
        
        pyrosim.End()

    def Create_Brain(self):
            pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
            pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
            pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
            pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
            pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
            pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
            pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
            pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
            pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
            pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
            
            pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +1 , jointName = "Torso_BackLeg")
            pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +2 , jointName = "Torso_FrontLeg")
            pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +3 , jointName = "Torso_LeftLeg")
            pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +4 , jointName = "Torso_RightLeg")
            pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +5 , jointName = "FrontLeg_FrontLowerLeg")
            pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +6 , jointName = "BackLeg_BackLowerLeg")
            pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +7 , jointName = "LeftLeg_LeftLowerLeg")
            pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +8 , jointName = "RightLeg_RightLowerLeg")
           
            for currentRow in range(c.numSensorNeurons): 
                for currentCol in range(c.numMotorNeurons): 
                    pyrosim.Send_Synapse(sourceNeuronName= currentRow, 
                                             targetNeuronName= currentCol+c.numSensorNeurons, 
                                             weight = self.weights[currentRow][currentCol])
                    #print(self.weights[currentRow][currentCol])
            pyrosim.End()
            
    def Mutate(self):
        row = random.randint(0, c.numSensorNeurons-1)
        col = random.randint(0, c.numMotorNeurons-1)
        self.weights[row, col] = random.random() * 2 -1
    
    def Set_ID(self, id):
        self.myID = id
        
        
        