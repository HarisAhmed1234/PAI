def lists_to_dict(keys, values):
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict

keys_list = input("Enter elements of the first list separated by spaces: ").split()
values_list = input("Enter elements of the second list separated by spaces: ").split()

if len(keys_list) != len(values_list):
    print("The lists must have the same number of elements.")
else:
    result = lists_to_dict(keys_list, values_list)
    print("Dictionary created from the lists:", result)
