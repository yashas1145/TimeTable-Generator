import random as rnd
from elements import Class

class schedule:
    def __init__(self, data):
        self.data, self._class, self._conflict = data, [], 0 
        self._fit, self._classNo, self._fitChange = -1, 0, True

    def getClass(self):
        self._fitChange = True
        return self._class

    def getConflict(self):
        return self._conflict

    def getFitness(self):
        if self._fitChange:
            self._fit = self.calculateFitness()
            self._fitChange = False
        
        return self._fit

    def initialize(self):
        dept = self.data.getDept()
        for i in range(len(dept)):
            course = dept[i].getCourse()
            for j in range(len(course)):
                newClass = Class(self._classNo, dept[i], course[j])
                self._classNo += 1
                newClass.setMeeting(self.data.getMeeting()[rnd.randrange(0, len(self.data.getMeeting()))])
                newClass.setRoom(self.data.getRoom()[rnd.randrange(0, len(self.data.getRoom()))])
                newClass.setFaculty(course[j].getFaculty()[rnd.randrange(0, len(course[j].getFaculty()))])
                self._class.append(newClass)
        return self

    def calculateFitness(self):
        self._conflict = 0
        classes = self.getClass()
        for i in range(len(classes)):
            if classes[i].getRoom().getCapacity() < classes[i].getCourse().getStudent(): self._conflict += 1
            
            for j in range(len(classes)):
                if j >= i:
                    if classes[i].getMeeting() == classes[j].getMeeting() and classes[i].getId() != classes[j].getId():
                        if classes[i].getRoom() == classes[j].getRoom(): self._conflict += 1
                        if classes[i].getFaculty() == classes[j].getFaculty(): self._conflict += 1
        return 1 / (1.0 * self._conflict + 1)

    def __str__(self):
        val = ""
        for i in range(len(self._class)-1):
            val += str(self._class[i]) + ", "
        val += str(self._class[len(self._class)-1])
        return val

class population:
    def __init__(self, size, data):
        self._size = size
        self._data = data
        self._schedule = []
        for i in range(size): 
            self._schedule.append(schedule(self._data).initialize())

    def getSchedule(self): return self._schedule