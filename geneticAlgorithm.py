import random as rnd
from schedule import population, schedule

class geneticAlgorithm:
    def __init__(self, numberOfEliteSchedule, popSize, mutationRate, tournamentSelectionSize, data):
        self.numberOfEliteSchedule, self.popSize, self.mutationRate, self.tournamentSelectionSize, self.data = numberOfEliteSchedule, popSize, mutationRate, tournamentSelectionSize, data
    def evolve(self, pop):
        return self.mutation(self.crossover(pop))

    def crossover(self, pop):
        crossoverPop = population(0, self.data)
        for i in range(self.numberOfEliteSchedule):
            crossoverPop.getSchedule().append(pop.getSchedule()[i])
        
        i = self.numberOfEliteSchedule
        while i < self.popSize:
            sch1 = self.selection(pop).getSchedule()[0]
            sch2 = self.selection(pop).getSchedule()[0]
            crossoverPop.getSchedule().append(self.crossoverSchedule(sch1, sch2))
            i += 1
        return crossoverPop

    def mutation(self, pop):
        for i in range(self.numberOfEliteSchedule, self.popSize):
            self.mutationSchedule(pop.getSchedule()[i])
        return pop

    def crossoverSchedule(self, sch1, sch2): 
        crossSchedule = schedule(self.data).initialize()
        for i in range(len(crossSchedule.getClass())):
            if rnd.random() > 0.5:
                crossSchedule.getClass()[i] = sch1.getClass()[i]
            else:
                crossSchedule.getClass()[i] = sch2.getClass()[i]
        return crossSchedule

    def mutationSchedule(self, mutateSch):
        sch = schedule(self.data).initialize()
        for i in range(len(mutateSch.getClass())):
            if self.mutationRate > rnd.random():
                mutateSch.getClass()[i] = sch.getClass()[i]
        return mutateSch

    def selection(self, pop):
        tournamentPop, i = population(0, self.data), 0
        while i < self.tournamentSelectionSize:
            tournamentPop.getSchedule().append(pop.getSchedule()[rnd.randrange(0, self.popSize)])
            i += 1
        tournamentPop.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
        return tournamentPop