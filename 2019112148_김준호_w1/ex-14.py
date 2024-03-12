# 2019112148 김준호

def combine_dictionaries(dic1, dic2):
    
    combined_dict = dic1.copy()

    for key, value in dic2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value

    return combined_dict

dic1 = {'a': 100, 'b': 200, 'c': 300}
dic2 = {'a': 200, 'b': 100, 'd': 400}

dic3 = combine_dictionaries(dic1, dic2)

print("Combined dictionary:", dic3)
