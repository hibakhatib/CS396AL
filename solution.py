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
        self.Create_Brain2(self.myID)
        self.random_quad()
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


        for i in np.arange(0, 0.1, c.length):
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
        


    def random_quad(self):
        pyrosim.Start_URDF("body.urdf")
        numLegs = c.limbs
        torso_len = c.length
        torso_width = c.width
        
        len_pos = []
        wid_pos = []
        for pos in np.arange(0,0.3,torso_len):
            len_pos.append(pos) # x
        for pos in np.arange(0,0.3,torso_width):
            wid_pos.append(pos) #y 
        
        k = 0
        j = 0
        
        torsoColor = random.randint(0,10)
        
        if torsoColor > 5:
            pyrosim.Send_Cube(name = "torso", pos = [-torso_len/3, 0, 1], size = [torso_len, torso_width, c.height], colorName = "green")
        else:
            pyrosim.Send_Cube(name = "torso", pos = [-torso_len/3, 0, 1], size = [torso_len, torso_width, c.height])
            
        
        for i in range(c.limbs):
            pyrosim.Send_Joint(name = "torso_limb" + str(j), parent = "torso", child = "limb" + str(j), type = "revolute", position = wid_pos[j], jointAxis = "1 1 0")
            pyrosim.Send_Cube(name )
            pyrosim.Send_Cube(name = "torso",
                              size = [c.length, c.width, c.height],
                              pos = [0,0,1],
                              colorName = "green"
                              )
        else:
            pyrosim.Send_Cube(name = "torso",
                              size = [c.length, c.width, c.height],
                              pos = [0,0,1]
                              )
            
        pyrosim.Send_Joint(name = "torso_link1",
                               parent = "torso",
                               child = "link1",
                               type = "revolute", 
                               position = [wid_pos[k], len_pos[j], 1], #im not sure this works
                               jointAxis = "1 1 0"
                               )
        
        for i in range(numLegs):
            if i in c.sensors:
                pyrosim.Send_Cube(name="Link" + str(i), pos=[wid_pos[k], len_pos[j], 1] , 
                                  size=[c.height, random.uniform(0.3,0.9), random.uniform(0.3,0.9)], 
                                  colorName = "green")
            else:
                pyrosim.Send_Cube(name="Link" + str(i), 
                                  pos=[wid_pos[k], len_pos[j], 1] , 
                                  size=[c.height, random.uniform(0.3,0.9), random.uniform(0.3,0.9)],)
            if i != numLegs - 1: return
            
            pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(i+1), parent = "Link" + str(i), child = "Link" + str(i+1), type = "revolute", 
                               position= [wid_pos[k], len_pos[j], 1], jointAxis = "1 1 0")
        
            k+=1
            j+=1
        pyrosim.End()
            
            
            
    
    
    
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