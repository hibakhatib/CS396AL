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
        
        self.links = {}
        self.joints = {}
        np.random.seed(1)

        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Brain()
        
        if c.id == 1:
            self.Create_Body()
        if c.id != 1:
            self.Create_Evolved()
        
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
            l =  round(c.limbs/2)
            pyrosim.Send_Cube(name="limb0", pos=[-c.limbs / 2,0,0.45], size=[l,1,0.5], colorName="green")
            
            
            left_start = 0.5 - l
            counter = 1
            k = 0
            for i in range(l):
                
                randSensor = random.randint(0,100)
                if randSensor >= 50:
                        color = "green"
                else:
                        color = "blue"
                
                pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [left_start,-0.5,0.45], jointAxis = "0 1 0")
                pyrosim.Send_Cube(name="limb" + str(counter), pos=[0,-0.15,0], size=[0.2,0.7,0.2], colorName="blue")
                
                self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                "parent": "limb0",
                                "child" : "limb" + str(counter),
                                "type" : "revolute",
                                "position": [left_start, -0.5, 0.45],
                                "jointAxis": "0 1 0"}
                
                self.links[k] = {"name": "limb" + str(counter),
                                "pos" : [0, -0.15, 0],
                                "size" : [0.2, 0.7, 0.2],
                                "colorName": "blue"}
                k +=1
                
                pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,-0.5,0], jointAxis = "1 0 0")
                pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.1], size = [0.2, 0.2, 0.7],  colorName=color)
                
                self.joints[k] = {"name" : "limb" + str(counter) + "_limb" + str(counter + 1), 
                                "parent": "limb" + str(counter),
                                "child" : "limb" + str(counter+1),
                                "type" : "revolute",
                                "position": [0,-0.5,0],
                                "jointAxis": "1 0 0"}
                
                self.links[k] = {"name": "limb" + str(counter+1),
                                "pos" : [0,0,-0.1],
                                "size" : [0.2, 0.2, 0.7],
                                "colorName": color}
                
                left_start+= 0.7
                counter+= 2
                k += 1

            right_start = 0.5 - l
            for i in range(l):
                
                randSensor = random.randint(0,100)
                if randSensor >= 50:
                    color = "green"
                else:
                    color = "blue"
                
                pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [right_start,0.5,0.45], jointAxis = "0 1 0")
                pyrosim.Send_Cube(name="limb" + str(counter), pos=[0,0.25,0], size=[0.2,0.7,0.2], colorName="blue")
                
                self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                "parent": "limb0",
                                "child" : "limb" + str(counter),
                                "type" : "revolute",
                                "position": [right_start,0.5,0.45],
                                "jointAxis": "0 1 0"}
                
                self.links[k] = {"name": "limb" + str(counter),
                                "pos" : [0, 0.25, 0],
                                "size" : [0.2, 0.7, 0.2],
                                "colorName": "blue"}

                k+=1
                
                pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,0.5,0], jointAxis = "1 0 0")
                pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.2], size = [0.2, 0.2, 0.7],  colorName=color)
                
                self.joints[k] = {"name" : "limb" + str(counter) + "_limb" + str(counter + 1), 
                                "parent": "limb" + str(counter),
                                "child" : "limb" + str(counter+1),
                                "type" : "revolute",
                                "position": [0,0.5,0],
                                "jointAxis": "1 0 0"}
                
                self.links[k] = {"name": "limb" + str(counter+1),
                                "pos" : [0,0,-0.2],
                                "size" : [0.2, 0.2, 0.7],
                                "colorName": color}
                right_start+=.5
                counter+= 2
                k+=1
                
            
            rand_size = [random.uniform(0.3,0.5),random.uniform(0.3, .7),random.uniform(0.1, 1)]
            pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [left_start,0,0.35], jointAxis = "0 0 1")
            pyrosim.Send_Cube(name="limb" + str(counter), pos=[-l,0,0.45], size=rand_size, colorName="blue")
            
            self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                "parent": "limb0",
                                "child" : "limb" + str(counter),
                                "type" : "revolute",
                                "position": [left_start,0,0.35],
                                "jointAxis": "1 0 1"}
                
            self.links[k] = {"name": "limb" + str(counter),
                                "pos" : [-l,0,0.45],
                                "size" : rand_size,
                                "colorName": "blue"}
            
            c.originLinks = self.links
            c.originJoints = self.joints
            c.id +=1
            pyrosim.End()
        

    def Create_Evolved(self):
    
            pyrosim.Start_URDF("body.urdf")
            l =  c.limbs
            pyrosim.Send_Cube(name="limb0", pos=[-c.limbs / 2,0,0.45], size=[l,1,0.5], colorName="green")
            
            random_limbs = random.randint(0,50)
            left_start = 0.5 - l
            counter = 1
            k = 0
            if random_limbs < 25:
                for i in range(l):
                    
                    randSensor = random.randint(0,100)
                    if randSensor >= 50:
                            color = "green"
                    else:
                            color = "blue"
                    
                    pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [left_start,-0.5,0.45], jointAxis = "0 1 0")
                    pyrosim.Send_Cube(name="limb" + str(counter), pos=[0,-0.15,0], size=[0.2,0.7,0.2], colorName="blue")
                    
                    self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                    "parent": "limb0",
                                    "child" : "limb" + str(counter),
                                    "type" : "revolute",
                                    "position": [left_start, -0.5, 0.45],
                                    "jointAxis": "0 1 0"}
                    
                    self.links[k] = {"name": "limb" + str(counter),
                                    "pos" : [0, -0.15, 0],
                                    "size" : [0.2, 0.7, 0.2],
                                    "colorName": "blue"}
                    k +=1
                    
                    pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,-0.5,0], jointAxis = "1 0 0")
                    pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.1], size = [0.2, 0.2, 0.7],  colorName=color)
                    
                    self.joints[k] = {"name" : "limb" + str(counter) + "_limb" + str(counter + 1), 
                                    "parent": "limb" + str(counter),
                                    "child" : "limb" + str(counter+1),
                                    "type" : "revolute",
                                    "position": [0,-0.5,0],
                                    "jointAxis": "1 0 0"}
                    
                    self.links[k] = {"name": "limb" + str(counter+1),
                                    "pos" : [0,0,-0.1],
                                    "size" : [0.2, 0.2, 0.7],
                                    "colorName": color}
                    
                    left_start+= 0.7
                    counter+= 2
                    k += 1
                    
            if random_limbs > 25:
                right_start = 0.5 - l
                for i in range(l):
                    
                    randSensor = random.randint(0,100)
                    if randSensor >= 50:
                        color = "green"
                    else:
                        color = "blue"
                    
                    pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [right_start,0.5,0.45], jointAxis = "0 1 0")
                    pyrosim.Send_Cube(name="limb" + str(counter), pos=[0,0.25,0], size=[0.2,0.7,0.2], colorName="blue")
                    
                    self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                    "parent": "limb0",
                                    "child" : "limb" + str(counter),
                                    "type" : "revolute",
                                    "position": [right_start,0.5,0.45],
                                    "jointAxis": "0 1 0"}
                    
                    self.links[k] = {"name": "limb" + str(counter),
                                    "pos" : [0, 0.25, 0],
                                    "size" : [0.2, 0.7, 0.2],
                                    "colorName": "blue"}

                    k+=1
                    
                    pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,0.5,0], jointAxis = "1 0 0")
                    pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.2], size = [0.2, 0.2, 0.7],  colorName=color)
                    
                    self.joints[k] = {"name" : "limb" + str(counter) + "_limb" + str(counter + 1), 
                                    "parent": "limb" + str(counter),
                                    "child" : "limb" + str(counter+1),
                                    "type" : "revolute",
                                    "position": [0,0.5,0],
                                    "jointAxis": "1 0 0"}
                    
                    self.links[k] = {"name": "limb" + str(counter+1),
                                    "pos" : [0,0,-0.2],
                                    "size" : [0.2, 0.2, 0.7],
                                    "colorName": color}
                    right_start+=.5
                    counter+= 2
                    k+=1
                
            
            rand_size = [random.uniform(0.3,0.5),random.uniform(0.3, .7),random.uniform(0.1, 1)]
            pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [left_start,0,0.35], jointAxis = "0 0 1")
            pyrosim.Send_Cube(name="limb" + str(counter), pos=[-l,0,0.45], size=rand_size, colorName="blue")
            
            self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                "parent": "limb0",
                                "child" : "limb" + str(counter),
                                "type" : "revolute",
                                "position": [left_start,0,0.35],
                                "jointAxis": "1 0 1"}
                
            self.links[k] = {"name": "limb" + str(counter),
                                "pos" : [-l,0,0.45],
                                "size" : rand_size,
                                "colorName": "blue"}
            
            c.originLinks = self.links
            c.originJoints = self.joints
            c.id +=1
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
        self.weights[row, col] = random.random() * 2 -1

    def Set_ID(self, id):
        self.myID = id
        
    def Evolved_Body(self):
        pyrosim.Start_URDF("body.urdf")
        l =  round(c.limbs/2)
        pyrosim.Send_Cube(name="limb0", pos=[-l / 2,0,0.45], size=[l,1,0.5], colorName="green")
            
        random_limb = random.randint(0,10000)
        left_start = 0.5 - l
        counter = 1
        k = 0
        for i in range(l):
                
                randSensor = random.randint(0,100)
                if randSensor >= 50:
                        color = "green"
                else:
                        color = "blue"
                        
                
                if random_limb > 5000:
                
                    pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [left_start,-0.5,0.45], jointAxis = "0 1 0")
                    pyrosim.Send_Cube(name="limb" + str(counter), pos=[0,-0.15,0], size=[0.2,0.7,0.2], colorName="blue")
                    
                    self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                    "parent": "limb0",
                                    "child" : "limb" + str(counter),
                                    "type" : "revolute",
                                    "position": [left_start, -0.5, 0.45],
                                    "jointAxis": "0 1 0"}
                    
                    self.links[k] = {"name": "limb" + str(counter),
                                    "pos" : [0, -0.15, 0],
                                    "size" : [0.2, 0.7, 0.2],
                                    "colorName": "blue"}
                    k +=1
                    
                
                    pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,-0.5,0], jointAxis = "1 0 0")
                    pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.1], size = [0.2, 0.2, 0.7],  colorName=color)
                    
                    self.joints[k] = {"name" : "limb" + str(counter) + "_limb" + str(counter + 1), 
                                    "parent": "limb" + str(counter),
                                    "child" : "limb" + str(counter+1),
                                    "type" : "revolute",
                                    "position": [0,-0.5,0],
                                    "jointAxis": "1 0 0"}
                    
                    self.links[k] = {"name": "limb" + str(counter+1),
                                    "pos" : [0,0,-0.1],
                                    "size" : [0.2, 0.2, 0.7],
                                    "colorName": color}
                    
                    left_start+= 0.7
                    counter+= 2
                    k += 1
                    
            
                
        right_start = 0.5 - l
        if l > 6:
                    l = l/2
        if random_limb >25000:
            for i in range(l):
                    randSensor = random.randint(0,100)
                    if randSensor >= 50:
                        color = "green"
                    else:
                        color = "blue"
                    
                    pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [right_start,0.5,0.45], jointAxis = "0 1 0")
                    pyrosim.Send_Cube(name="limb" + str(counter), pos=[0,0.25,0], size=[0.2,0.7,0.2], colorName="blue")
                    
                    self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                    "parent": "limb0",
                                    "child" : "limb" + str(counter),
                                    "type" : "revolute",
                                    "position": [right_start,0.5,0.45],
                                    "jointAxis": "0 1 0"}
                    
                    self.links[k] = {"name": "limb" + str(counter),
                                    "pos" : [0, 0.25, 0],
                                    "size" : [0.2, 0.7, 0.2],
                                    "colorName": "blue"}

                    k+=1
                    
                    pyrosim.Send_Joint( name = "limb" + str(counter) + "_limb" + str(counter + 1) , parent= "limb" + str(counter), child = "limb" + str(counter + 1), type = "revolute", position = [0,0.5,0], jointAxis = "1 0 0")
                    pyrosim.Send_Cube(name="limb" + str(counter + 1), pos=[0,0,-0.2], size = [0.2, 0.2, 0.7],  colorName=color)
                    
                    self.joints[k] = {"name" : "limb" + str(counter) + "_limb" + str(counter + 1), 
                                    "parent": "limb" + str(counter),
                                    "child" : "limb" + str(counter+1),
                                    "type" : "revolute",
                                    "position": [0,0.5,0],
                                    "jointAxis": "1 0 0"}
                    
                    self.links[k] = {"name": "limb" + str(counter+1),
                                    "pos" : [0,0,-0.2],
                                    "size" : [0.2, 0.2, 0.7],
                                    "colorName": color}
                    right_start+=.5
                    counter+= 2
                    k+=1
                    
                
            rand_size = [random.uniform(0.3,0.5),random.uniform(0.3, .7),random.uniform(0.1, 1)]
            pyrosim.Send_Joint( name = "limb0_limb" + str(counter) , parent= "limb0", child = "limb" + str(counter), type = "revolute", position = [left_start,0,0.35], jointAxis = "0 0 1")
            pyrosim.Send_Cube(name="limb" + str(counter), pos=[-l,0,0.45], size=rand_size, colorName="blue")
                
            self.joints[k] = {"name" : "limb0_limb" + str(counter), 
                                    "parent": "limb0",
                                    "child" : "limb" + str(counter),
                                    "type" : "revolute",
                                    "position": [left_start,0,0.35],
                                    "jointAxis": "1 0 1"}
                    
            self.links[k] = {"name": "limb" + str(counter),
                                    "pos" : [-l,0,0.45],
                                    "size" : rand_size,
                                    "colorName": "blue"}
                
            c.originLinks = self.links
            c.originJoints = self.joints
            c.id +=1
            pyrosim.End()
        

    # def Evolved_Body2(self):
    #     pyrosim.Start_URDF("body.urdf")
        
    #     rand_limb = random.randint(1, round(len(c.originLinks)/2) -1)
    #     print(rand_limb)
       
        
    #     originLen = len(c.originLinks)
    #     originJoints = len(c.originJoints)
    #     if len(c.originLinks) > 1:
            
    #         del(c.originLinks[rand_limb])
    #         del(c.originJoints[rand_limb])
    #         c.newLinks = len(c.originLinks)
    #         c.newJoints = len(c.originJoints)


    #     if originLen != c.newLinks:
    #         names = [i for i in range(c.newLinks)]
    #         j = 0
    #         for i in c.originLinks.values():
    #             lst = list(i.values())
    #             pyrosim.Send_Link(name = "limb" + str(names[j]), pos = lst[1], size = lst[2], colorName = lst[3])
    #             j+=1
            
    #     if originJoints != c.newJoints:
    #         names = [i for i in range(c.newJoints)]
    #         j = 0
    #         for i in c.originJoints.values():
    #             lst = list(i.values())
    #             pyrosim.Send_Joint(name = lst[0], parent = lst[1], child = lst[2], type = lst[3], position = lst[4], jointAxis = lst[5])
        
    #     c.id +=1
    #     pyrosim.End()