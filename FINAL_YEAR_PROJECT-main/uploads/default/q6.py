def odd_index_elements(lst):
    return [lst[i] for i in range(1, len(lst), 2)]


input_list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Input:", input_list1)
print("Output:", odd_index_elements(input_list1))


input_list2 = [23, 46, 69, 92, 115]
print("Input:", input_list2)
print("Output:", odd_index_elements(input_list2))
