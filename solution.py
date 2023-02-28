import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random 
import time
import constants as c



class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
        self.myID = nextAvailableID
        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Brain()
        self.Create_Body()
        os.system("python simulate.py " + directOrGUI + " " + str(self.myID) + " &")
        
    def Wait_For_Simulation_To_End(self):
        fitFile = "fitness" + str(self.myID) + ".txt"
        motorFile = "motor" + str(self.myID) + ".txt"
        while not os.path.exists(fitFile):
            time.sleep(1/100)
        
        fitnessFile = open(fitFile, "r")
        fit = fitnessFile.read()
        self.fitness = float(fit)
        fitnessFile.close()
        os.system("del " + fitFile)
        
        # mFile = open(motorFile, "r")
        # motor = mFile.read()
        # self.motor = (motor)
        # mFile.close()
        # os.system("del " + motorFile)
        
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
        
    def Create_Body(self):
            
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="limb0", pos=[-c.limbs / 2,0,0.45], size=[c.limbs,1,0.5], colorName="green")
        
        left_start = 0.5 - c.limbs
        counter = 1

        for i in range(c.limbs):
            
            randSensor = random.randint(0,100)
            if randSensor >= 50:
                    color = "green"
            else:
                    color = "blue"
            
            pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [left_start,-0.5,0.45], jointAxis = "0 1 0")
            pyrosim.Send_Cube(name="limb" + str(counter), pos=[0,-0.25,0], size=[0.2,0.5,0.2], colorName="blue")
            
            pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,-0.5,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.2], size=[random.uniform(0.1, 0.3),random.uniform(0.3, 0.5),random.uniform(0.1, 1)],  colorName=color)

            left_start+= 1
            counter+= 2

        
        right_start = 0.5 - c.limbs
        for i in range(c.limbs):
            
            randSensor = random.randint(0,100)
            if randSensor >= 50:
                color = "green"
            else:
                color = "blue"
            
            pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [right_start,0.5,0.45], jointAxis = "0 1 0")
            pyrosim.Send_Cube(name="limb" + str(counter), pos=[0,0.25,0], size=[0.2,0.5,0.2], colorName="blue")
            
            pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,0.5,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.2], size=[random.uniform(0.1, 0.3),random.uniform(0.3, 0.5),random.uniform(0.1, 0.8)],  colorName=color)

            right_start+=1
            counter+= 2
            
        pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [right_start-c.limbs,0,0.35], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="limb" + str(counter), pos=[random.uniform(1, 1.5),0,0.45], size=[random.uniform(0.1, 0.3),random.uniform(0.3, 0.5),random.uniform(0.1, 1)], colorName="blue")
        print(counter)
        breakpoint()
        

        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "limb0")
        limbCounter = 1
        for i in range(1, c.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = limbCounter , linkName = "limb" + str(i))
            limbCounter +=1
        
        for i in range(c.numMotorNeurons):
            pyrosim.Send_Motor_Neuron( name = limbCounter , jointName = "limb0_limb" + str(i * 2 + 1))
            limbCounter +=1
        
        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
        
    
    def Mutate(self):
        row = random.randint(0, c.numSensorNeurons-1)
        col = random.randint(0, c.numMotorNeurons-1)
        self.weights[row, col] = random.random() * 2 - 1
    
    def Set_ID(self, id):
        self.myID = id

        
        

    # def Create_Body(self):
            
    #         pyrosim.Start_URDF("simple.urdf")
    #                     #hexapod final
    #         pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[c.length+1.5, c.width, c.height])
    #         pyrosim.Send_Cube(name="LeftLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
    #         pyrosim.Send_Cube(name="RightLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
    #         pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
    #         pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
    #         pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-1, -0.5, 1], jointAxis="0 0 1")
    #         pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[-1, 0.5, 1], jointAxis="0 0 1")
    #         pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="0 1 0")
    #         pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="0 1 0")


    #         pyrosim.Send_Cube(name="LeftLeg2", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
    #         pyrosim.Send_Cube(name="RightLeg2", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
    #         pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
    #         pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
    #         pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2", type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
    #         pyrosim.Send_Joint(name="LeftLeg2_LeftLowerLeg2", parent="LeftLeg2", child="LeftLowerLeg2", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
    #         pyrosim.Send_Joint(name="RightLeg2_RightLowerLeg2", parent="RightLeg2", child="RightLowerLeg2", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
    #         pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2", type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0 ")

    #         pyrosim.Send_Cube(name="LeftLeg3", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
    #         pyrosim.Send_Cube(name="RightLeg3", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
    #         pyrosim.Send_Cube(name="LeftLowerLeg3", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
    #         pyrosim.Send_Cube(name="RightLowerLeg3", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
    #         pyrosim.Send_Joint(name="Torso_LeftLeg3", parent="Torso", child="LeftLeg3", type="revolute", position=[1, -0.5, 1], jointAxis="0 0 1")
    #         pyrosim.Send_Joint(name="Torso_RightLeg3", parent="Torso", child="RightLeg3", type="revolute", position=[1, 0.5, 1], jointAxis="0 0 1")
    #         pyrosim.Send_Joint(name="LeftLeg3_LeftLowerLeg3", parent="LeftLeg3", child="LeftLowerLeg3", type="revolute", position=[0, -1, 0], jointAxis="0 1 0")
    #         pyrosim.Send_Joint(name="RightLeg3_RightLowerLeg3", parent="RightLeg3", child="RightLowerLeg3", type="revolute", position=[0, 1, 0], jointAxis="0 1 0")
    #         pyrosim.End()
            
        
    # def Create_Brain2(self, ID):
    #     pyrosim.Start_NeuralNetwork("brain" + str(ID) + ".nndf")
    #     names = 0
    #     if c.length + 1 in c.sensors:
    #         pyrosim.Send_Sensor_Neuron(name = names , linkName = "Head")
    #         pyrosim.Send_Motor_Neuron( name = names + 1 , jointName = "Head_Link1")
    #         names += 2


    #     for i in np.arange(0, 0.1, c.length):
    #         if i in c.sensors:
    #             pyrosim.Send_Sensor_Neuron(name = names , linkName = "Link" + str(i))
    #             names += 1
    #             if i == c.length - 1: continue
    #             pyrosim.Send_Motor_Neuron( name = names , jointName = "Link" + str(i) + "_Link" + str(i+1))
    #             names += 1
                
    #     for currentRow in range(c.numSensorNeurons):
    #         for currentColumn in range(c.numMotorNeurons):
    #             pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

    #     pyrosim.End()
    
    # def Create_Brain(self):
    #         pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    #         pyrosim.Send_Sensor_Neuron(name=0, linkName="LeftLowerLeg")
    #         pyrosim.Send_Sensor_Neuron(name=1, linkName="RightLowerLeg")
    #         pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg2")
    #         pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg2")
    #         pyrosim.Send_Sensor_Neuron(name=4, linkName="LeftLowerLeg3")
    #         pyrosim.Send_Sensor_Neuron(name=5, linkName="RightLowerLeg3")
            
            
    #         pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
    #         pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")
    #         pyrosim.Send_Motor_Neuron(name=8, jointName="LeftLeg_LeftLowerLeg")
    #         pyrosim.Send_Motor_Neuron(name=9, jointName="RightLeg_RightLowerLeg")
    #         pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_LeftLeg2")
    #         pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_RightLeg2")
    #         pyrosim.Send_Motor_Neuron(name=12, jointName="LeftLeg2_LeftLowerLeg2")
    #         pyrosim.Send_Motor_Neuron(name=13, jointName="RightLeg2_RightLowerLeg2")
    #         pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_LeftLeg3")
    #         pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_RightLeg3")
    #         pyrosim.Send_Motor_Neuron(name=16, jointName="LeftLeg3_LeftLowerLeg3")
    #         pyrosim.Send_Motor_Neuron(name=17, jointName="RightLeg3_RightLowerLeg3")
           
    #         for currentRow in range(c.numSensorNeurons): 
    #             for currentCol in range(c.numMotorNeurons): 
    #                 pyrosim.Send_Synapse(sourceNeuronName= currentRow, 
    #                                          targetNeuronName= currentCol+c.numSensorNeurons, 
    #                                          weight = self.weights[currentRow][currentCol])
    #                 #print(self.weights[currentRow][currentCol])
    #         pyrosim.End()
        
    # def Create_Random(self):
    #     length = c.length
    #     pyrosim.Start_URDF("limb.urdf")
    #     if length + 1 in c.sensors:
    #         pyrosim.Send_Cube(name="Head", pos=[-10,20,2.5] , 
    #                           size=[random.randint(1,3), random.randint(1,6), random.randint(1,5)], 
    #                           colorName="green")
    #     else:
    #         pyrosim.Send_Cube(name="Head", pos=[-10,20,2.5] , 
    #                           size=[random.randint(1,3), random.randint(1,6), random.randint(1,5)])
    #     pyrosim.Send_Joint(name = "Head_Link1", parent = "Head", child = "Link1", type = "revolute", 
    #                        position= [-10,15-(random.randint(1,6))/2,2.5], jointAxis = "0 0 1")

    #     for i in range(length):
    #         if i in c.sensors:
    #             pyrosim.Send_Cube(name="Link" + str(i), pos=[0,(-(random.randint(0,5))/2),0] , 
    #                               size=[random.randint(1,5), ((random.randint(0,5))), random.randint(1,5)], 
    #                               colorName = "green")
    #         else:
    #             pyrosim.Send_Cube(name="Link" + str(i), 
    #                               pos=[0,(-(random.randint(0,5))/2),0] , 
    #                               size=[random.randint(1,5), ((random.randint(0,5))), random.randint(1,5)])
    #         if i != length - 1: return
            
    #         pyrosim.Send_Joint(name = "Link" + str(i) + "_Link" + str(i+1), parent = "Link" + str(i), child = "Link" + str(i+1), type = "revolute", 
    #                            position= [0,(-(random.randint(0,5))/2),0], jointAxis = "0 0 1")

    #     pyrosim.End()
        


    # def random_quad(self):
    #     pyrosim.Start_URDF("limb.urdf")
    #     torso_len = c.length
    #     torso_width = c.width
    #     torso_height = c.height
        
    #     len_pos = []
    #     wid_pos = []
    #     len_pos = np.arange(0,torso_len, 0.3)
    #     wid_pos = np.arange(0,torso_width, 0.3)
    #     #     len_pos.append(pos) # x
    #     # for pos in np.arange(0,0.3,torso_width):
    #     #     wid_pos.append(pos) #y 
        
    #     k = 0
    #     j = 0
        
    #     if len(len_pos) < len(wid_pos):
    #         empty_posns = len_pos
    #     else:
    #         empty_posns = wid_pos
        
    #     torsoColor = random.randint(0,10)
        
    #     if torsoColor > 5:
    #         pyrosim.Send_Cube(name = "limb0", pos = [-torso_len/2, 0, 1], size = [torso_len, torso_width, torso_height], colorName = "green")
    #     else:
    #         pyrosim.Send_Cube(name = "limb0", pos = [-torso_len/2, 0, 1], size = [torso_len, torso_width, torso_height])
        
        
    #     limbCounter = 1
    #     for i in range(len(empty_posns)):
    #         saved_h = c.height
    #         color_pick = random.randint(0,10)
    #         if color_pick > 5:
    #             color = "green"
    #         else:
    #             color = "blue"
    #         pyrosim.Send_Joint( name = "limb0_limb" + str(limbCounter) , parent= "limb0", child = "limb" + str(limbCounter), type = "revolute", position = [len_pos[j], -wid_pos[j], saved_h], jointAxis = "0 0 1")
    #         pyrosim.Send_Cube(name="limb" + str(limbCounter), pos=[len_pos[j], wid_pos[j], saved_h], size=[c.length, c.width, c.height], colorName = color)
            
    #         pyrosim.Send_Joint( name = "limb" + str(limbCounter) + "_limb" + str(limbCounter + 1) , parent= "limb" + str(limbCounter), child = "limb" + str(limbCounter + 1), type = "revolute", position = [len_pos[j],-wid_pos[j], saved_h], jointAxis = "0 0 1")
    #         pyrosim.Send_Cube(name="limb" + str(limbCounter + 1), pos=[len_pos[j]+ 0.3, 0, wid_pos[j]+ 0.3], size=[c.length, c.width, c.height], colorName = color)

    #         limbCounter +=2
    #         j+=1

    #     for i in range(len(empty_posns)):
    #         color_pick = random.randint(0,10)
    #         if color_pick > 5:
    #             color = "green"
    #         else:
    #             color = "blue"
    #         saved_h = c.height
    #         pyrosim.Send_Joint( name = "limb0_limb" + str(limbCounter) , parent= "limb0", child = "limb" + str(limbCounter), type = "revolute", position = [len_pos[k]/2, wid_pos[k]/2, saved_h], jointAxis = "0 0 1")
    #         pyrosim.Send_Cube(name="limb" + str(limbCounter), pos=[len_pos[k], wid_pos[k], saved_h], size=[c.length, c.width, c.height], colorName = color)
            
    #         pyrosim.Send_Joint( name = "limb" + str(limbCounter) + "_limb" + str(limbCounter + 1) , parent= "limb" + str(limbCounter), child = "limb" + str(limbCounter + 1), type = "revolute", position = [len_pos[k],wid_pos[k], saved_h], jointAxis = "0 0 1")
    #         pyrosim.Send_Cube(name="limb" + str(limbCounter + 1), pos=[(len_pos[k]/2)+ 0.3, 0, wid_pos[k]+ 0.3], size=[c.length, c.width, c.height], colorName = color)

    #         limbCounter +=2
    #         k+=1

    #     pyrosim.End()
    
            
