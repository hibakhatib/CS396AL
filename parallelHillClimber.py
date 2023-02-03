from solution import SOLUTION 
import constants as c
import copy 
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        
        for file in os.listdir(r"C:\Users\hibar\CS396AL2"):
            if file.startswith("brain"):
                os.system("rm brain*.nndf")
            if file.startswith("fitness"):
                os.system("rm fitness*.txt")
        self.nextAvailableID =0
        self.parents = {}
        for i in range(c.population):
            self.nextAvailableID += 1
            self.parents[i] = SOLUTION(self.nextAvailableID)

            
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        
    
    def Evaluate(self, solutions):
        for sol in solutions:
            solutions[sol].Start_Simulation("DIRECT")
        for sol in solutions:
            solutions[sol].Wait_For_Simulation_To_End()
    
        
    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()

    def Print(self):
        for parent in self.parents:
            print(f"\nparent fitness {self.parent.fitness}, child fitness {self.child.fitness}")
        
    def Select(self):
        for parent in self.parents:
            if self.parents[parent].fitness > self.children[parent].fitness:
                self.parents[parent] = self.children[parent]
                
    def Show_Best(self):
        highest_fitness = 0
        for k in self.parents.keys():
            parent = self.parents[k]
            if(parent.fitness < highest_fitness):
                best = parent
                highest_fitness = parent.fitness
        best.Start_Simulation("GUI")