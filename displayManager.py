import prettytable as pt

class displayManager:

    def __init__(self, data):
        self.data = data

    def printAvailableData(self):
        print("Master data")
        self.printDept()
        self.printCourse()
        self.printRoom()
        self.printMeeting()
        self.printFaculty()

    def printDept(self):
        dept = self.data.getDept()
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
        course = self.data.getCourse()
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
        faculty = self.data.getFaculty()
        for i in range(len(faculty)):
            table.add_row([faculty[i].getId(), faculty[i].getName()])
        print(table)

    def printMeeting(self):
        table = pt.PrettyTable(['Id', 'Time'])
        meeting = self.data.getMeeting()
        for i in range(len(meeting)):
            table.add_row([meeting[i].getId(), meeting[i].getTime()])

    def printRoom(self):
        table = pt.PrettyTable(['Room Number', 'Capacity'])
        room = self.data.getRoom()
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