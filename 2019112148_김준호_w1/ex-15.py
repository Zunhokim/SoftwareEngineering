# 2019112148 김준호

dic1 = {'item1': 45.50, 'item2':35, 'item3':41.30, 'item4':55, 'item5': 24}

sorted_dict = sorted(dic1.items(), key= lambda item:item[1], reverse=True)

print(sorted_dict[:3])