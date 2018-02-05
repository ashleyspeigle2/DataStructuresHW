##Ashley Speigle
##Lab04: Simulation Part 2
import random

patients = ["Bob", "Herbert", "Joe", "Suzy", "Bertha", "Alice", "Don", "Billy", "Andrew",
           "George","Fred", "Cain", "Adam", "Eve", "Peter", "Noel", "Ashley", "Linda",
           "Richard", "Brandon"]
           
class patient:
    def __init__(self,name):
        self.name = name

def nurse(wr):
    wr.addPatients2(wr.removePatients())
    

class waitingRoom:
    # keep track of patients before nurse
    def __init__(self):
        self.patientsWaiting = []
        self.patientsWaitingForever = []
    def addPatients(self,patient):
        self.patientsWaiting.append(patient)
    def removePatients(self):
        return self.patientsWaiting.pop(0)
    # keep track of patients waiting to see physician or not
    def addPatients2(self,patient):
        self.patientsWaitingForever.append(patient)
    def removePatients2(self):
        return self.patientsWaitingForever.pop(0)
    def emptyRoom(self): #tells if room is empty
        if self.patientsWaiting == []:
            return True
        else:
            return False

    def emptyRoom2(self): #tells if room is empty
        if self.patientsWaitingForever == []:
            return True
        else:
            return False


class examRoom:
    
    def __init__(self):
        self.roomTime = 0
        self.patient = None
        self.patientTime = 0 #tells how long the patient should be in room

    def addPatients4(self,wr):
        #go to waiting room
        self.patient = wr.removePatients2()
        self.patientTime = random.randrange(15,21)

    def time(self):
        return self.patientTime

    def emptyRoom(self): #tells if room is empty
        if self.patient == None:
            return True
        else:
            return False

    def removePatients4(self):
        x = self.patient
        self.patient = None
        return x
    #assign physician for exam rooms
        
    #keep track how long the patient has been in the room
    def timeSpentInRoom(self):
        return self.roomTime

    def increasedTime(self):
        self.roomTime += 1


#advance time w/ for
w = waitingRoom()

e1 = examRoom()
e2 = examRoom()
e3 = examRoom()
e4 = examRoom()
e5 = examRoom()
e6 = examRoom()

for y in patients:
    w.addPatients(y)
    
def updateTime():
    nurse(w)
    if not e1.emptyRoom():
        e1.increasedTime()
        if e1.time() >= e1.timeSpentInRoom():
            e1.removePatients4()
            
    if e1.emptyRoom():
        if not w.emptyRoom2():
            e1.addPatients4(w)

    if not e2.emptyRoom():
        e2.increasedTime()
        if e2.time() >= e2.timeSpentInRoom():
            e2.removePatients4()
            
    if e2.emptyRoom():
        if not w.emptyRoom2():
            e2.addPatients4(w)

    if not e3.emptyRoom():
        e3.increasedTime()
        if e3.time() >= e3.timeSpentInRoom():
            e3.removePatients4()
            
    if e3.emptyRoom():
        if not w.emptyRoom2():
            e3.addPatients4(w)

    if not e4.emptyRoom():
        e4.increasedTime()
        if e4.time() >= e4.timeSpentInRoom():
            e4.removePatients4()
            
    if e4.emptyRoom():
        if not w.emptyRoom2():
            e4.addPatients4(w)

    if not e5.emptyRoom():
        e5.increasedTime()
        if e5.time() >= e5.timeSpentInRoom():
            e5.removePatients4()
            
    if e5.emptyRoom():
        if not w.emptyRoom2():
            e5.addPatients4(w)

    if not e6.emptyRoom():
        e6.increasedTime()
        if e6.time() >= e6.timeSpentInRoom():
            e1.removePatients4()
            
    if e6.emptyRoom():
        if not w.emptyRoom2():
            e6.addPatients4(w)
        
        
        

    
