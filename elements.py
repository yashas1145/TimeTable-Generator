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