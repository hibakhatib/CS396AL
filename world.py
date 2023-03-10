
import pybullet as p
import pyrosim as pyrosim 
import pybullet_data

class WORLD:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8) 
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
        #pyrosim.End()