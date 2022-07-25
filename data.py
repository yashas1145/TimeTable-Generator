from elements import room, faculty, meetingTime, course, department

class Data:
    rooms = {"R1":25, "R2":45, "R3":35}
    instructor = {"I1":"KSR", "I2":"VKB", "I3":"NNC", "I4":"KVS"}
    meetingTime = {"MT1":"MWFS 09:00-10:00", "MT2":"MWFS 12:00-13:00", "MT3":"TTHS 09:00-10:00", "MT4":"TTHS 11:00-12:00", "MT5":"MWF 13:45-14:45"}

    def __init__(self):
        self._room, self._meeting, self._instructors = [], [], []
        for i in self.rooms:
            self._room.append(room(i, self.rooms[i]))

        for i in self.meetingTime:
            self._meeting.append(meetingTime(i, self.meetingTime[i]))
        
        for i in self.instructor:
            self._instructors.append(faculty(i, self.instructor[i]))

        course1=course("C1","325K",[self._instructors[0],self._instructors[1]],25)
        course2=course("C2","319K",[self._instructors[0],self._instructors[1],self._instructors[2]],35)
        course3=course("C3","42k",[self._instructors[0],self._instructors[1]],25)
        course4=course("C4","464K",[self._instructors[2],self._instructors[3]],30)
        course5=course("C5","360C",[self._instructors[3]],35)
        course6=course("C6","303K",[self._instructors[0],self._instructors[2]],45)
        course7=course("C7","303L",[self._instructors[1],self._instructors[3]],45)
        self._course = [course1,course2,course3,course4,course5,course6,course7]

        dept1 = department("MATH",[course1,course3])
        dept2 = department("EE",[course2,course4,course5])
        dept3 = department("PHY",[course6,course7])
        self._dept = [dept1,dept2,dept3]

        self._numberOfClass = 0
        for i in range(len(self._dept)):
            self._numberOfClass += len(self._dept[i].getCourse())

    def getRoom(self): return self._room
    def getFaculty(self): return self._instructors
    def getCourse(self): return self._course
    def getDept(self): return self._dept
    def getClassNumber(self): return self._numberOfClass
    def getMeeting(self): return self._meeting




    