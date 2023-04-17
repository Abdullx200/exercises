# Write your code here

def merge_dicts(dictionary_1, dictionary_2):
    new_dict= {}
    for i in dictionary_1:
        new_dict[i] = dictionary_1[i]
    for j in dictionary_2:
        new_dict[j] = dictionary_2[j]

    return new_dict