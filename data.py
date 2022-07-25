from elements import room, faculty, meetingTime, course, department

class Data:
    #JSON/Dicts/HashMaps
    rooms = {"R1":60, "R2":60, "R3":60}

    instructor = {"I1":"KSR", "I2":"NSL", "I3":"SK",
                    "I4":"VKB", "I5":"PGS", "I6":"KVS",
                    "I7":"SS", "I8":"RSR", "I9":"BNR",
                    "I10":"PMR", "I11":"NKB", "I12":"PBM"}

    meetingTime = {"MT1":"MWFS 09:00-10:00",
                    "MT2":"MWFS 12:00-13:00", 
                    "MT3":"TThS 09:00-10:00", 
                    "MT4":"TThS 11:00-12:00", 
                    "MT5":"MWF 13:45-14:45",
                    "MT6":"TWThF 15:45-16:45"}

    def __init__(self):
        self._room, self._meeting, self._instructors = [], [], []
        for i in self.rooms:
            self._room.append(room(i, self.rooms[i]))

        for i in self.meetingTime:
            self._meeting.append(meetingTime(i, self.meetingTime[i]))
        
        for i in self.instructor:
            self._instructors.append(faculty(i, self.instructor[i]))

        course1 = course("C1", "18CS61A", [self._instructors[0]], 50)
        course2 = course("C2", "18CS61B", [self._instructors[1]], 50)
        course3 = course("C3", "18CS61C", [self._instructors[2]], 50)
        course4 = course("C4", "18CS62A", [self._instructors[3]], 50)
        course5 = course("C5", "18CS62B", [self._instructors[4]], 50)
        course6 = course("C6", "18CS62C", [self._instructors[5]], 50)
        course7 = course("C7", "18CS63A", [self._instructors[6]], 50)
        course8 = course("C8", "18CS63B", [self._instructors[7]], 50)
        course9 = course("C9", "18CS63C", [self._instructors[8]], 50)
        course10 = course("C10", "18CS641A", [self._instructors[10]], 50)
        course11 = course("C11", "18CS641B", [self._instructors[11]], 50)
        course12 = course("C12", "18CS643A", [self._instructors[9]], 50)
        self._course = [course1,course2,course3,course4,course5,course6,course7,course8,course9,course10,course11,course12]

        dep1 = department("CSE", self._course)
        self._dept = [dep1]

        self._numberOfClass = 0
        for i in range(len(self._dept)):
            self._numberOfClass += len(self._dept[i].getCourse())

    def getRoom(self): return self._room
    def getFaculty(self): return self._instructors
    def getCourse(self): return self._course
    def getDept(self): return self._dept
    def getClassNumber(self): return self._numberOfClass
    def getMeeting(self): return self._meeting