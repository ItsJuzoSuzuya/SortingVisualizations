import time

class BubbleSort:
    def __init__(self, myList):
        self.myList = myList

    def sort(self, wait_time=0.02):
        start = time.time()
        listSorted = False
        length = len(self.myList) - 1

        while not listSorted:
            check = True
            
            for i in range(length):
          #      time.sleep(wait_time)
                if self.myList[i] > self.myList[i + 1]:
                    self.myList[i], self.myList[i + 1] = self.myList[i + 1], self.myList[i]
                    check = False
                    self.visualizator.drawList(self.myList)
                    
            if check:
                listSorted = True
            else: length -=  1
        end = time.time()
        print(end - start)
