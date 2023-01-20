import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1


def Generate_Body():
    pyrosim.Start_URDF("simple.urdf")
    pyrosim.Send_Cube(name = "Torso", pos = [1.5,0,1.5], size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name = "Backleg", pos = [-.5, 0, -.5], size=[length,width,height])
    pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name = "Frontleg", pos = [0.5, 0, -.5], size=[length,width,height])
    pyrosim.End()
    
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[1,5,0] , size=[length,width,height])
    pyrosim.End()
    
    
def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    pyrosim.End()
    
# def Create_Robot():
#     pyrosim.Start_URDF("body.urdf")
#     pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[length,width,height])
#     pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
#     pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5] , size=[length,width,height])
#     pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
#     pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5] , size=[length,width,height])
#     pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0] , size=[length,width,height])    
#     pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,0.5,0.5])
#     pyrosim.Send_Cube(name="Link4", pos=[0,0.5,0] , size=[length,width,height]) 
#     pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,1,0])
#     pyrosim.Send_Cube(name = "Link5", pos = [0, -1, -1], size=[length,width,height])
#     pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [0,1.5,0])
#     pyrosim.Send_Cube(name = "Link6", pos = [0, -2.5 ,-2], size=[length,width,height])
#     pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [0,1.5,0])
#     pyrosim.End()
    
    
    


#pyrosim.Send_Cube(name="Box2", pos=[0,1,1] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box3", pos=[0,0,0] , size=[length,width,height])
Generate_Body()
Generate_Brain()


    