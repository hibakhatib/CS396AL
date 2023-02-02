
import pybullet as p
import pyrosim as pyrosim 
import pybullet_data

class WORLD:
    def __init__(self):

        #self.physicsClient = p.connect(p.DIRECT)
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
        #pyrosim.End()