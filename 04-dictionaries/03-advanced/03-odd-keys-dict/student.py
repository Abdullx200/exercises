# Write your code here
def odd_keys_dict(geg):
    odd = {}
    sleutels = geg.keys()
    for i in sleutels:
        if i%2 >=1:
                odd[i] = geg[i]

    return odd