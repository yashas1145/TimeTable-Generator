import random as rnd, prettytable as pt
from datetime import datetime as dt

class Data:
    rooms = [["A301", 50],["A302", 50],["A303", 50], ["A312", 50],["A313", 50],["A314", 50]]
    instructor = [["I1","KSR"], ["I2","VKB"], ["I3","NSL"], ["I4","SM"], ["I5","KVS"], ["I6","SS"], ["I7","SK"], ["I8","SBG"]]
    meetingTime = [["MT1","M 09:00-10:00"], ["MT2","M 10:00-11:00"], ["MT3","M 11:00-12:00"], ["MT4","M 12:00-13:00"], ["MT5","M 13:45-14:45"], ["MT6","M 14:45-15:45"], ["MT7","M 15:45-16:45"],
                   ["MT8","T 09:00-10:00"], ["MT9","T 10:00-11:00"], ["MT10","T 11:00-12:00"], ["MT11","T 12:00-13:00"], ["MT12","T 13:45-14:45"], ["MT13","T 14:45-15:45"], ["MT14","T 15:45-16:45"],
                   ["MT15","W 09:00-10:00"], ["MT16","W 10:00-11:00"], ["MT17","W 11:00-12:00"], ["MT18","W 12:00-13:00"], ["MT19","W 13:45-14:45"], ["MT20","W 14:45-15:45"], ["MT21","W 15:45-16:45"],
                   ["MT22","Th 09:00-10:00"], ["MT23","Th 10:00-11:00"], ["MT24","Th 11:00-12:00"], ["MT25","Th 12:00-13:00"], ["MT26","Th 13:45-14:45"], ["MT27","Th 14:45-15:45"], ["MT28","Th 15:45-16:45"],
                   ["MT29","F 09:00-10:00"], ["MT30","F 10:00-11:00"], ["MT31","F 11:00-12:00"], ["MT32","F 12:00-13:00"], ["MT33","F 13:45-14:45"], ["MT34","F 14:45-15:45"], ["MT35","F 15:45-16:45"],
                   ["MT36","S 09:00-10:00"], ["MT37","S 10:00-11:00"], ["MT38","S 11:00-12:00"], ["MT39","S 12:00-13:00"]]

    def __init__(self):
        self._room, self._meeting, self._instructors = [], [], []
        for i in range(len(self.rooms)):
            self._room.append(room(self.rooms[i][0], self.rooms[i][1]))

        for i in range(len(self.meetingTime)):
            self._meeting.append(meetingTime(self.meetingTime[i][0], self.meetingTime[i][1]))
        
        for i in range(len(self.instructor)):
            self._instructors.append(faculty(self.instructor[i][0], self.instructor[i][1]))


        course1=course("C1","18CS31",[self._instructors[0],self._instructors[1]],25)
        course2=course("C2","18CS32",[self._instructors[0],self._instructors[1],self._instructors[2]],35)
        course3=course("C3","18CS33",[self._instructors[0],self._instructors[1]],25)
        course4=course("C4","18CS34",[self._instructors[2],self._instructors[3]],30)
        course5=course("C5","18CS35",[self._instructors[3]],35)
        course6=course("C6","18CS36",[self._instructors[0],self._instructors[2]],45)
        course7=course("C7","18CS51",[self._instructors[0],self._instructors[1]],25)
        course8=course("C8","18CS52",[self._instructors[0],self._instructors[1],self._instructors[2]],35)
        course9=course("C9","18CS53",[self._instructors[0],self._instructors[1]],25)
        course10=course("C10","18CS54",[self._instructors[2],self._instructors[3]],30)
        course11=course("C11","18CS55",[self._instructors[3]],35)
        course12=course("C12","18CS56",[self._instructors[0],self._instructors[2]],45)
        course13=course("C13","18CS71",[self._instructors[0],self._instructors[1]],25)
        course14=course("C14","18CS72",[self._instructors[0],self._instructors[1],self._instructors[2]],35)
        course15=course("C15","18CS73",[self._instructors[0],self._instructors[1]],25)
        course16=course("C16","18CS74",[self._instructors[2],self._instructors[3]],30)
        course17=course("C17","18CS75",[self._instructors[3]],35)
        course18=course("C18","18CS76",[self._instructors[0],self._instructors[2]],45)
        
        
        
        # self._course = [course1,course2,course3,course4,course5,course6,course7,course8,course9,course10,course11,course12,course13,course14,course15,course16,course17,course18,course19,course20,course21,course22,course23,course24]
        self._course = [course1,course2,course3,course4,course5,course6,course7,course8,course9,course10,course11,course12,course13,course14, course15, course17, course18]

        # dept1 = department("CSE",[course1, course2, course3, course4, course5, course6,course7,course8,course9,course10,course11,course12,course13,course14,course15,course16,course17,course18,course19,course20,course21,course22,course23,course24])
        dept1 = department("CSE",[course1, course2, course3, course4, course5, course6,course7,course8,course9,course10,course11,course12,course13,course14, course15, course17, course18])
        self._dept = [dept1]

        self._numberOfClass = 0
        for i in range(len(self._dept)):
            self._numberOfClass += len(self._dept[i].getCourse())

    def getRoom(self): return self._room
    def getFaculty(self): return self._instructors
    def getCourse(self): return self._course
    def getDept(self): return self._dept
    def getClassNumber(self): return self._numberOfClass
    def getMeeting(self): return self._meeting

class schedule:
    def __init__(self):
        self._data, self._class, self._conflict = data, [], 0 
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
        dept = self._data.getDept()
        for i in range(len(dept)):
            course = dept[i].getCourse()
            for j in range(len(course)):
                newClass = Class(self._classNo, dept[i], course[j])
                self._classNo += 1
                newClass.setMeeting(data.getMeeting()[rnd.randrange(0, len(data.getMeeting()))])
                newClass.setRoom(data.getRoom()[rnd.randrange(0, len(data.getRoom()))])
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
        return 1 / ((1.0 * self._conflict + 1))

    def __str__(self):
        val = ""
        for i in range(len(self._class)-1):
            val += str(self._class[i]) + ", "
        val += str(self._class[len(self._class)-1])
        return val

class population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedule = []
        for i in range(size): self._schedule.append(schedule().initialize())

    def getSchedule(self):
        return self._schedule

class course:
    def __init__(self, number, name, faculty, student):
        self.number = number
        self.name = name
        self.faculty = faculty
        self.student = student

    def __str__(self):
        return self.name

    def getNumber(self): return self.number
    def getName(self): return self.name
    def getFaculty(self): return self.faculty
    def getStudent(self): return self.student

class faculty:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def getId(self): return self.id
    def getName(self): return self.name

class room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def getNumber(self): return self.number
    def getCapacity(self): return self.capacity

class meetingTime:
    def __init__(self, id, time):
        self._id, self._time = id, time

    def getId(self): return self._id
    def getTime(self): return self._time

class department:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def getName(self): return self.name
    def getCourse(self): return self.course

class Class:
    def __init__(self, id, dept, course):
        self.id = id
        self.dept = dept
        self.course = course
        self.faculty = None
        self.room = None
        self.meeting = None

    def __str__(self):
        return "{},{},{},{},{}".format(str(self.dept.getName()), str(self.course.getNumber()), str(self.room.getNumber()), str(self.faculty.getId()), str(self.meeting.getId()))

    def getId(self): return self.id
    def getDept(self): return self.dept
    def getCourse(self): return self.course
    def getFaculty(self): return self.faculty
    def getRoom(self): return self.room
    def getMeeting(self): return self.meeting

    def setFaculty(self, faculty): self.faculty = faculty 
    def setRoom(self, room): self.room = room
    def setMeeting(self, meeting): self.meeting = meeting

class displayManager:

    def printAvailableData(self):
        print("Master data")
        self.printDept()
        self.printCourse()
        self.printRoom()
        self.printMeeting()
        self.printFaculty()

    def printDept(self):
        dept = data.getDept()
        table = pt.PrettyTable(['Department', 'Courses'])
        for i in range(len(dept)):
            course = dept.__getitem__(i).getCourse()
            tempStr = "["
            for j in range(len(course)-1):
                tempStr += course[j].__str__() + ", "
            tempStr += course[len(course)-1].__str__() + "]"
            table.add_row([dept.__getitem__(i).getName(), tempStr])
        print(table)

    def printCourse(self):
        table = pt.PrettyTable(['Id', 'Course code', 'Max number of students', 'Faculty'])
        course = data.getCourse()
        for i in range(len(course)):
            faculty = course[i].getFaculty()
            tempStr = ""
            for j in range(len(faculty)-1):
                tempStr += faculty[j].__str__() + ", "
            tempStr += faculty[len(faculty)-1].__str__()
            
            table.add_row([course[i].getNumber(), course[i].getName(), str(course[i].getStudent()), tempStr])
        print(table)            

    def printFaculty(self):
        table = pt.PrettyTable(['Id', 'Faculty'])
        faculty = data.getFaculty()
        for i in range(len(faculty)):
            table.add_row([faculty[i].getId(), faculty[i].getName()])
        print(table)

    def printMeeting(self):
        table = pt.PrettyTable(['Id', 'Time'])
        meeting = data.getMeeting()
        for i in range(len(meeting)):
            table.add_row([meeting[i].getId(), meeting[i].getTime()])

    def printRoom(self):
        table = pt.PrettyTable(['Room Number', 'Capacity'])
        room = data.getRoom()
        for i in range(len(room)):
            table.add_row([room[i].getNumber(), room[i].getCapacity()])
        print(table)

    def printGeneration(self, pop):
        table = pt.PrettyTable(['Schedule', 'Fitness', 'Conflicts'])
        schedule = pop.getSchedule()
        for i in range(len(schedule)):
            table.add_row([str(i), round(schedule[i].getFitness(), 3), schedule[i].getConflict()])
        print(table)

    def printSchedule(self, schedule):
        classes = schedule.getClass()
        table = pt.PrettyTable(['Class', 'Dept', 'Course', 'Room', 'Faculty', 'Time'])
        for i in range(len(classes)):
            table.add_row([str(i), classes[i].getDept().getName(), classes[i].getCourse().getName(), classes[i].getRoom().getNumber(), classes[i].getFaculty().getName(), classes[i].getMeeting().getTime()])
        print(table)

class geneticAlgorithm:
    def evolve(self, pop):
        return self.mutation(self.crossover(pop))

    def crossover(self, pop):
        crossoverPop = population(0)
        for i in range(numberOfEliteSchedule):
            crossoverPop.getSchedule().append(pop.getSchedule()[i])
        
        i = numberOfEliteSchedule
        while i < popSize:
            sch1 = self.selection(pop).getSchedule()[0]
            sch2 = self.selection(pop).getSchedule()[0]
            crossoverPop.getSchedule().append(self.crossoverSchedule(sch1, sch2))
            i += 1
        return crossoverPop

    def mutation(self, pop):
        for i in range(numberOfEliteSchedule, popSize):
            self.mutationSchedule(pop.getSchedule()[i])
        return pop

    def crossoverSchedule(self, sch1, sch2):
        crossSchedule = schedule().initialize()
        for i in range(len(crossSchedule.getClass())):
            if rnd.random() > 0.5:
                crossSchedule.getClass()[i] = sch1.getClass()[i]
            else:
                crossSchedule.getClass()[i] = sch2.getClass()[i]
        return crossSchedule

    def mutationSchedule(self, mutateSch):
        sch = schedule().initialize()
        for i in range(len(mutateSch.getClass())):
            if mutationRate > rnd.random():
                mutateSch.getClass()[i] = sch.getClass()[i]
        return mutateSch

    def selection(self, pop):
        tournamentPop, i = population(0), 0
        while i < tournamentSelectionSize:
            tournamentPop.getSchedule().append(pop.getSchedule()[rnd.randrange(0, popSize)])
            i += 1
        tournamentPop.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
        return tournamentPop

startTime = dt.now()

popSize = 2
data = Data()
disp = displayManager()
disp.printAvailableData()
gen = 0
print("\nGENERATION " + str(gen))
pop = population(popSize)
pop.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
disp.printGeneration(pop)
disp.printSchedule(pop.getSchedule()[0])

numberOfEliteSchedule = 1
tournamentSelectionSize = 3
mutationRate = 0.1

ga = geneticAlgorithm()
while pop.getSchedule()[0].getFitness() != 1.0:
    gen += 1
    print("Generation {}".format(gen))
    pop = ga.evolve(pop)
    pop.getSchedule().sort(key=lambda x: x.getFitness(), reverse=True)
    disp.printGeneration(pop)
    disp.printSchedule(pop.getSchedule()[0])

print("Execution time: {} seconds".format(dt.now()-startTime))