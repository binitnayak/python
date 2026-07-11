from  random import randint
class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no :{self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train  no :{self.trainNo} is running on time ")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no :{self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t=train(12999)
t.book("delhi","ranchi")
t.getstatus()
t.getFare("delhi","ranchi")