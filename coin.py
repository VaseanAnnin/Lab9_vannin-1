import random 

class coin:
    def __init__(self):
        self.__sideup = "HEADS"

    def toss(self):
        rand_num = random.randint(0,1)

        if rand_num == 0:
            self.__sideup = "TAILS"
        else:
            self.__sideup = "HEADS"