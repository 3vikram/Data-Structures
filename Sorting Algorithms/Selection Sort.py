def find_smallest_number_index(lst):
    smallestNumber = lst[0]
    for lst_elements in range(len(lst)):
        if smallestNumber > lst[lst_elements]:
            smallestNumber = lst[lst_elements]

    return lst.index(smallestNumber)

def selection_sort(lst):
    temp_lst = []
    actual_list_length = len(lst)
    i = 0
    while i <= actual_list_length-1:
        smallest_index = find_smallest_number_index(lst)
        temp_lst.append(lst[smallest_index])
        del lst[smallest_index]
        i += 1

    return temp_lst


if __name__ == '__main__':
    numb_list = [4,3,90,98,34,43,-989,-1]
    print(selection_sort(numb_list))


'''
Output:

[-989, -1, 3, 4, 34, 43, 90, 98]
'''
