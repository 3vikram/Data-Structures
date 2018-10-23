def find_largest_number(lst):
    largestNumber = lst[0]
    for lst_elements in range(len(lst)):
        if largestNumber < lst[lst_elements]:
            largestNumber = lst[lst_elements]
        elif largestNumber > lst[lst_elements]:
            continue
        elif largestNumber == lst[lst_elements]:
            continue

    return largestNumber


if __name__ == '__main__':
    numb_list = [4,3,90,98,34,43,989]
    print("The largest number in an array is {0}".format(find_largest_number(numb_list)))

'''
Output:

The largest number in an array is 989
'''
