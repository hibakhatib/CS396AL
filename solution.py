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
        self.weights[random.randint(0, c.numSensorNeurons-1), 
                     random.randint(0, c.numMotorNeurons-1)] = random.random() * 2 - 1
        self.links = []
        self.joints = []
        rand_seed = nextAvailableID*random.randint(0,3)
        np.random.seed(rand_seed)
        self.Create_Body()

        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Brain()
        self.Create_Body()
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
        pyrosim.End()
        
    def Create_Body(self):
            
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="limb0", pos=[-c.limbs / 2,0,0.45], size=[c.limbs,1,0.5], colorName="green")
        self.links.append([0, "limb0"])
        
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
            self.links.append([i, "limb" + str(counter)])
            self.joints.append([i, "limb0_limb" + str(counter)])
            
            pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,-0.5,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.2], size = [0.2, 0.3, 0.2],  colorName=color)
            self.links.append([i, "limb" + str(counter+1)])
            self.joints.append([i, "limb0_limb" + str(counter+1)])

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
            self.links.append([i, "limb" + str(counter)])
            self.joints.append([i, "limb0_limb" + str(counter)])
            
            pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,0.5,0], jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.2], size = [0.2, 0.3, 0.2],  colorName=color)
            self.links.append([i, "limb" + str(counter+1)])
            self.joints.append([i, "limb0_limb" + str(counter+1)])

            right_start+=1
            counter+= 2
            
        pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [right_start-c.limbs,0,0.35], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="limb" + str(counter), pos=[random.uniform(1, 1.5),0,0.45], size=[random.uniform(0.1, 0.3),random.uniform(0.3, 0.5),random.uniform(0.1, 1)], colorName="blue")
        self.links.append([i+1, "limb" + str(counter)])
        self.joints.append([i+1, "limb0_limb" + str(counter)])
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
        remove_rand = random.randint(0, len(self.links)-1)
        # self.links.pop(remove_rand)
        # self.joints.pop(remove_rand-2)
        if c.limbs > 10:
            c.limbs = random.randint(4,8)
            if c.limbs %2 != 0:
                c.limbs = c.limbs *2 -1
        else:
            c.limbs = random.randint(2, 6)
            if c.limbs %2 != 0:
                c.limbs = c.limbs *2 -1

    
    def Set_ID(self, id):
        self.myID = id

        
