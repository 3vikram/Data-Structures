def find_smallest_number(lst):
    smallestNumber = lst[0]
    for lst_elements in range(len(lst)):
        if smallestNumber > lst[lst_elements]:
            smallestNumber = lst[lst_elements]
        elif smallestNumber < lst[lst_elements]:
            continue
        elif smallestNumber == lst[lst_elements]:
            continue

    return smallestNumber


if __name__ == '__main__':
    numb_list = [4,3,90,98,34,43,989,-1]
    print("The largest number in an array is {0}".format(find_largest_number(numb_list)))

'''
Output:
The largest number in an array is -1
'''
