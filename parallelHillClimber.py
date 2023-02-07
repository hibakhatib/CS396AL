from solution import SOLUTION 
import constants as c
import copy 
import os
import random


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        
        
        for id in range(c.population):
            for file in os.listdir(r"."):
                if file.startswith(f"brain{id}"):
                    os.system(f"del brain{id}.nndf")
                if file.startswith(f"fitness{id}"):
                    os.system(f"del fitness{id}.txt")
            
            # os.system("del brain" + str(id) + ".nndf")
            # os.system("del fitness" + str(id) + ".txt")
                
        self.nextAvailableID = 0
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
        for sol in range(c.population):
            solutions[sol].Start_Simulation("DIRECT")
        for sol in range(c.population):
            solutions[sol].Wait_For_Simulation_To_End()
    
        
    def Spawn(self):
        self.children = {}
        for parent in self.parents.keys():
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Mutate(self):
        for i in self.children.keys():
            self.children[i].Mutate()

    def Print(self):
        for parent in self.parents.keys():
            print(f"\nparent fitness {self.parents[parent].fitness}")
        
        for child in self.children.keys():
            print(f"child fitness {self.children[child].fitness}")
        
    def Select(self):
        for parent in self.parents.keys():
            if self.parents[parent].fitness > self.children[parent].fitness:
                self.parents[parent] = self.children[parent]
                
    def Show_Best(self):
        highest_fitness = 1000
        for k in self.parents.keys():
            parent  = self.parents[k]
            if(parent.fitness > highest_fitness):
                best = parent
                highest_fitness = parent.fitness
                best.Start_Simulation("GUI")
        
    def Show_Random(self):
        i = len(self.parents.keys())
        r = random.randint(0,i)
        best_rand = self.parents[r]
        best_rand.Start_Simulation("GUI")