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
        #self.Create_Random()
        #self.Create_Body()
        self.Create_Brain3()
        self.Create_Ant()
        # self.Random_Morphology()
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
        #pyrosim.Send_Cube(name="Box", pos=[-2,-2,0.5] , size=[c.length, c.width, c.height])
        pyrosim.End()
        
        

    def Create_Body(self):
            
            pyrosim.Start_URDF("simple.urdf")
                        #hexapod final
            pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[c.length+1.5, c.width, c.height])
            pyrosim.Send_Cube(name="LeftLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
            pyrosim.Send_Cube(name="RightLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
            pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
            pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
            pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-1, -0.5, 1], jointAxis="0 0 1")
            pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[-1, 0.5, 1], jointAxis="0 0 1")
            pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="0 1 0")
            pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="0 1 0")


            pyrosim.Send_Cube(name="LeftLeg2", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
            pyrosim.Send_Cube(name="RightLeg2", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
            pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
            pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
            pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2", type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
            pyrosim.Send_Joint(name="LeftLeg2_LeftLowerLeg2", parent="LeftLeg2", child="LeftLowerLeg2", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
            pyrosim.Send_Joint(name="RightLeg2_RightLowerLeg2", parent="RightLeg2", child="RightLowerLeg2", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
            pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2", type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0 ")

            pyrosim.Send_Cube(name="LeftLeg3", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
            pyrosim.Send_Cube(name="RightLeg3", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
            pyrosim.Send_Cube(name="LeftLowerLeg3", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
            pyrosim.Send_Cube(name="RightLowerLeg3", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
            pyrosim.Send_Joint(name="Torso_LeftLeg3", parent="Torso", child="LeftLeg3", type="revolute", position=[1, -0.5, 1], jointAxis="0 0 1")
            pyrosim.Send_Joint(name="Torso_RightLeg3", parent="Torso", child="RightLeg3", type="revolute", position=[1, 0.5, 1], jointAxis="0 0 1")
            pyrosim.Send_Joint(name="LeftLeg3_LeftLowerLeg3", parent="LeftLeg3", child="LeftLowerLeg3", type="revolute", position=[0, -1, 0], jointAxis="0 1 0")
            pyrosim.Send_Joint(name="RightLeg3_RightLowerLeg3", parent="RightLeg3", child="RightLowerLeg3", type="revolute", position=[0, 1, 0], jointAxis="0 1 0")
            pyrosim.End()
        
        
    def Create_Brain2(self, ID):
        pyrosim.Start_NeuralNetwork("brain" + str(ID) + ".nndf")


        names = 0
        if c.length + 1 in c.sensors:
            pyrosim.Send_Sensor_Neuron(name = names , linkName = "Head")
            pyrosim.Send_Motor_Neuron( name = names + 1 , jointName = "Head_Link1")
            names += 2


        for i in range(c.length):
            if i in c.sensors:
                pyrosim.Send_Sensor_Neuron(name = names , linkName = "Link" + str(i))
                names += 1
                if i == c.length - 1: continue
                pyrosim.Send_Motor_Neuron( name = names , jointName = "Link" + str(i) + "_Link" + str(i+1))
                names += 1
                
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
    
    def Create_Brain(self):
            pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
            pyrosim.Send_Sensor_Neuron(name=0, linkName="LeftLowerLeg")
            pyrosim.Send_Sensor_Neuron(name=1, linkName="RightLowerLeg")
            pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg2")
            pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg2")
            pyrosim.Send_Sensor_Neuron(name=4, linkName="LeftLowerLeg3")
            pyrosim.Send_Sensor_Neuron(name=5, linkName="RightLowerLeg3")
            
            
            pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
            pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")
            pyrosim.Send_Motor_Neuron(name=8, jointName="LeftLeg_LeftLowerLeg")
            pyrosim.Send_Motor_Neuron(name=9, jointName="RightLeg_RightLowerLeg")
            pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_LeftLeg2")
            pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_RightLeg2")
            pyrosim.Send_Motor_Neuron(name=12, jointName="LeftLeg2_LeftLowerLeg2")
            pyrosim.Send_Motor_Neuron(name=13, jointName="RightLeg2_RightLowerLeg2")
            pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_LeftLeg3")
            pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_RightLeg3")
            pyrosim.Send_Motor_Neuron(name=16, jointName="LeftLeg3_LeftLowerLeg3")
            pyrosim.Send_Motor_Neuron(name=17, jointName="RightLeg3_RightLowerLeg3")
           
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
        self.weights[row, col] = random.random() * 2 - 1
    
    def Set_ID(self, id):
        self.myID = id
        
    def Create_Random(self):
        length = c.length
        pyrosim.Start_URDF("body.urdf")
        if length + 1 in c.sensors:
            pyrosim.Send_Cube(name="Head", pos=[-10,20,2.5] , 
                              size=[random.randint(1,3), random.randint(1,6), random.randint(1,5)], 
                              colorName="green")
        else:
            pyrosim.Send_Cube(name="Head", pos=[-10,20,2.5] , 
                              size=[random.randint(1,3), random.randint(1,6), random.randint(1,5)])
        pyrosim.Send_Joint(name = "Head_Link1", parent = "Head", child = "Link1", type = "revolute", 
                           position= [-10,15-(random.randint(1,6))/2,2.5], jointAxis = "0 0 1")

        for i in range(length):
            if i in c.sensors:
                pyrosim.Send_Cube(name="Link" + str(i), pos=[0,(-(random.randint(0,5))/2),0] , 
                                  size=[random.randint(1,5), ((random.randint(0,5))), random.randint(1,5)], 
                                  colorName = "green")
            else:
                pyrosim.Send_Cube(name="Link" + str(i), 
                                  pos=[0,(-(random.randint(0,5))/2),0] , 
                                  size=[random.randint(1,5), ((random.randint(0,5))), random.randint(1,5)])
            if i != length - 1: return
            
            pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(i+1), parent = "Link" + str(i), child = "Link" + str(i+1), type = "revolute", 
                               position= [0,(-(random.randint(0,5))/2),0], jointAxis = "0 0 1")

        pyrosim.End()
        
    def Create_Ant(self):
        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Link(name = "body", pos = [0,0,0], size = [random.uniform(0.8,3),random.uniform(0.8,3),random.uniform(0.8,3)], colorName = "blue")
        pyrosim.End()
    
    def Create_Brain3(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="base")
        pyrosim.End()
        

        #legs must be able to connect to any random unoccupied point to main Link/body
        #leg sizes random 
        #max number of legs is as many as can fit around the main body without overcrowding/overlapping as described in project desc
        #

    # def Random_Morphology(self):
    #     pyrosim.Start_URDF("simple.urdf")
    #     pyrosim.Send_Cube(name="Head", pos=[0,0,1] , size=[c.length+1.5, c.width, c.height])
    #     init_z = 1
    #     possible_len = random.randint(2,9) #number of links
    #     num_joints = possible_len - 1
    #     sensors = [False] * possible_len
    #     sensors[random.randint(0,possible_len-1)]
    #     joint_type = ['slider', 'revolute', 'continuous']
    #     for i in range(possible_len):
    #         j = random.randint(0, possible_len)
    #         for i in range(j):
    #             init_z += 1
    #             pyrosim.Send_Cube(name = f"{i}", pos = [0,0,(init_z +1)], size = [random.randint(0,5), random.randint(0,5), random.randint(0,5)])
    #             for k in range((possible_len) - j):
    #                 prev_k = k-1
    #                 rand_joint = joint_type[random.randint(0,3) -1]
    #                 pyrosim.Send_Joint(name = f"{prev_k}_{k}", parent = f"{prev_k}", child = f"{k}", type = f"{rand_joint}", position = [0,0, (init_z + 1)], jointAxis = "0 1 0")
                    
    #     pyrosim.End()
    
    
    
    def random_quad(self):
        pyrosim.Start_URDF("simple.urdf")
        torso_size = [random.uniform(.3,5), random.uniform(0.3,5), random.uniform(0, 1)]
        
        
        numLegs = random.randint(1,6)
    
    
    
    #     def Create_Body(self):
        #     pyrosim.Start_URDF("simple.urdf")
            
        #     pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[c.length, c.width, c.height])
        #     pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2, 1, 0.2])
        #     pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2, 1, 0.2])
        #     pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        #     pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
            
        #     pyrosim.Send_Cube(name = "LeftLeg", pos = [-0.5,0,0], size = [1, 0.2, 0.2])
        #     pyrosim.Send_Cube(name = "RightLeg", pos = [0.5,0,0], size = [1, 0.2, 0.2])
        #     pyrosim.Send_Joint(name = "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-.5,0,1], jointAxis = "0 1 0")
        #     pyrosim.Send_Joint(name = "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [.5,0,1], jointAxis = "0 1 0")
            
        #     pyrosim.Send_Cube(name = "BackLowerLeg", pos = [0,0,-0.5], size = [0.2, 0.2, 1])
        #     pyrosim.Send_Cube(name = "FrontLowerLeg", pos = [0,0,-0.5], size = [0.2, 0.2, 1])
        #     pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg", parent = "FrontLeg", child = "FrontLowerLeg", type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        #     pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg", parent = "BackLeg", child = "BackLowerLeg", type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
            
        #     pyrosim.Send_Cube(name = "LeftLowerLeg", pos = [0,0,-0.5], size = [0.2, 0.2,1])
        #     pyrosim.Send_Cube(name = "RightLowerLeg", pos = [0,0,-0.5], size = [0.2, 0.2,1])
        #     pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg", parent = "LeftLeg", child = "LeftLowerLeg", type = "revolute", position = [-1, 0,0], jointAxis = "0 1 0")
        #     pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg", parent = "RightLeg", child = "RightLowerLeg", type = "revolute", position = [1, 0,0], jointAxis = "0 1 0")
            
        #     pyrosim.End()

    # def Create_Brain(self):
    #         pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    #         pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    #         pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    #         pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    #         pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
    #         pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
    #         pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
    #         pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
    #         pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
    #         pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
            
    #         pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +1 , jointName = "Torso_BackLeg")
    #         pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +2 , jointName = "Torso_FrontLeg")
    #         pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +3 , jointName = "Torso_LeftLeg")
    #         pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +4 , jointName = "Torso_RightLeg")
    #         pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +5 , jointName = "FrontLeg_FrontLowerLeg")
    #         pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +6 , jointName = "BackLeg_BackLowerLeg")
    #         pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +7 , jointName = "LeftLeg_LeftLowerLeg")
    #         pyrosim.Send_Motor_Neuron(name = c.numMotorNeurons +8 , jointName = "RightLeg_RightLowerLeg")
           
    #         for currentRow in range(c.numSensorNeurons): 
    #             for currentCol in range(c.numMotorNeurons): 
    #                 pyrosim.Send_Synapse(sourceNeuronName= currentRow, 
    #                                          targetNeuronName= currentCol+c.numSensorNeurons, 
    #                                          weight = self.weights[currentRow][currentCol])
    #                 #print(self.weights[currentRow][currentCol])
    #         pyrosim.End()