#Kelvin Soto (no group)
#Learned about the update() method here: https://www.w3schools.com/python/ref_dictionary_update.asp


def return_dict(string):
    string = string.replace(' ', '')
    dict = {}
    char_list = set(string.lower())
    count = 0
    for i in char_list:
        dict.update({i : string.count(i)})
    return dict

string = input('Enter a string: ')
dict = return_dict(string)
print(dict)
