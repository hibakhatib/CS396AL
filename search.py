# import os
# import generate
# import simulate

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")

from hillclimber import HILLCLIMBER 

hc = HILLCLIMBER()
hc.Evolve()

