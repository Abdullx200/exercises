class AssocList:
    def __init__(self):
        # Initialize an empty list to store key-value pairs
        self.__items = []

    def __setitem__(self, key, value):
        # Find the index of the key in the list
        index = self.__find_key_index(key)

        # If the key is not in the list, add a new key-value pair
        if index == -1:
            self.__items.append([key, value])
        # Otherwise, update the value associated with the key
        else:
            self.__items[index][1] = value

    def __contains__(self, key):
        # Check if the key is present in the list
        return self.__find_key_index(key) != -1

    def __getitem__(self, key):
        # Find the index of the key in the list
        index = self.__find_key_index(key)

        # If the key is not in the list, raise a KeyError
        if index == -1:
            raise KeyError()
        # Otherwise, return the value associated with the key
        else:
            return self.__items[index][1]

    def __len__(self):
        # Return the number of key-value pairs in the list
        return len(self.__items)

    def __find_key_index(self, key):
        # Search for the key in the list and return its index
        for i in range(len(self.__items)):
            k, v = self.__items[i]
            if k == key:
                return i
        # If the key is not found, return -1
        return -1

    @property
    def keys(self):
        # Return a list of all the keys in the list
        return [k for k, _ in self.__items]

    @property
    def values(self):
        # Return a list of all the values in the list
        return [v for _, v in self.__items]
