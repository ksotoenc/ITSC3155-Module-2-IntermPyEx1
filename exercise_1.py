#Kelvin Soto (no group)

# I used this link to figure out what the built-in "set()" function does: 
# https://www.programiz.com/python-programming/methods/built-in/set

def create_unique_list(sample_list):
    return set(sample_list)

list = [1, 2, 3, 2, 1, 4]
unique_list = create_unique_list(list)
print(unique_list)