class Queue():
    def __init__(self):
        self.__Queue =[]
        
    def add(self, item):
        self.__Queue.append(item)

    def next(self):
        item = self.__Queue[0]
        del self.__Queue[0]
        return item
    
    def is_empty(self):
        return len(self.__Queue) == 0
