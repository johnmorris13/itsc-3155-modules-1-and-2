def get_combined_dict(dict1,dict2):
    combined={}
    common=set(dict1.keys())&set(dict2.keys())
    for x in common:
        combined[x]=dict1[x]+dict2[x]
    return combined

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)