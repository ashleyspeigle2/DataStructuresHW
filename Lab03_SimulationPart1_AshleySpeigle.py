##Ashley Speigle
##Lab03: Simulation

class patient:
    def __init__(self,name):
        self.name = name

class physician:
    # give examination (15-20 mins)
    def examination(self):
        pass
                 
class nurse:
    def __init__(self, nurse1):
        pass
    # gets patient from waiting room
    def getPatient(self):
        pass
    # send to 2nd waiting room queue
    def sendPatient(self):
        pass


class waitingRoom:
    # keep track of patients before nurse
    def __init__(self):
        self.patientsWaiting = []
        self.patientsWaitingForever = []
    def addPatients(self,patient):
        self.patientsWaiting.append(patient)
    def removePatients(self):
        return patientsWaiting.pop(0)
    # keep track of patients waiting to see physician or not
    def addPatients2(self,patient):
        self.patientsWaitingForever.append(patient)
    def removePatients2(self):
        return patientsWaitingForever.pop(0)

class examRoom:
    def __init__(self,physician1):
        self.physician = physician1
        self.roomTime = 0
        self.patient = None

    def addPatients4(self,waitingRoom):
        self.physician.append(waitingRoom)

    def removePatients4(self):
        return physician.pop(0)
    #assign physician for exam rooms
        
    #add/remove patient
    #keep track how long the patient has been in the room
    def timeSpentInRoom(self):
        return self.roomTime
    


#advance time w/ for loop
while True:
    p = patient("Herbert")
    
    w = waitingRoom()
    
    e1 = examRoom()
    e2 = examRoom()
    e3 = examRoom()
    e4 = examRoom()
    e5 = examRoom()
    e6 = examRoom()


    
    
    
