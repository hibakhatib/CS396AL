# import os
# import generate
# import simulate

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")



from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
phc.Show_Random()