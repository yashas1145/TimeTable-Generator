from datetime import datetime as dt
from displayManager import displayManager
from data import Data
from schedule import population
from geneticAlgorithm import geneticAlgorithm

startTime = dt.now()

popSize = 10
data = Data()
disp = displayManager(data)
disp.printAvailableData()
gen = 0
print("\nGENERATION " + str(gen))
pop = population(popSize, data)
pop.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
disp.printGeneration(pop)
disp.printSchedule(pop.getSchedule()[0])

numberOfEliteSchedule = 1
tournamentSelectionSize = 3
mutationRate = 0.1

ga = geneticAlgorithm(numberOfEliteSchedule, popSize, mutationRate, tournamentSelectionSize, data)
while pop.getSchedule()[0].getFitness() != 1.0:
    gen += 1
    print("Generation {}".format(gen))
    pop = ga.evolve(pop)
    pop.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
    disp.printGeneration(pop)
    disp.printSchedule(pop.getSchedule()[0])

print("Execution time: {} seconds".format(dt.now()-startTime))