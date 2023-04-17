class CircularBuffer:
    
    def __init__(self, maxsize):
        self.__maxsize = maxsize
        self.__items = []

    def __len__(self):
        return len(self.__items)

    def add(self, item):
        self.__items.append(item)
        if len(self.__items )> self.__maxsize:
            del self.__items[0]

    def __getitem__(self, index):
        return self.__items[index]
            