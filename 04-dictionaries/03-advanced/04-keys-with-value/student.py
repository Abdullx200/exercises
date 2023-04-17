# Write your code here
def keys_with_value(dictionary, value):
    lijst = []
    sleutelts = dictionary.keys()
    for i in sleutelts:
        if dictionary[i] == value:
            lijst.append(i)

    return lijst