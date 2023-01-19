#Kelvin Soto (no group)

#Used this website to learn how to append keys to an empty dictionary:
#https://www.digitalocean.com/community/tutorials/python-add-to-dictionary


def get_combined_dict(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    combined_dict = {}
    for key in common_keys:
        combined_dict[key] =  dict1.get(key) + dict2.get(key)
    return combined_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)