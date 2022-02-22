def get_max_from_dict_of_lists(dict):
    max_key = None
    max_value = 0
    for (key, list) in dict.items():
        value = len(list) # Here the function
        if max_key == None or value > max_value:
            max_value = value
            max_key = key
    
    return (max_key, max_value)

def remove_key_from_dict(dict, key):
    del dict[key]

def remove_from_dict(dict, key):

    for l in dict[key]:
        c_list = dict[l]
        c_list.remove(key)
        dict[l] = c_list

    remove_key_from_dict(dict, key)

