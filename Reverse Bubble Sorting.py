def Reverse_Bubble_Sort(lst):
    
    if len(lst) == 1:
        return lst
    
    for sorting in range(0, len(lst)-1):
        flag = False
        for element in range(1, len(lst)):
            if lst[element-1] < lst[element]:
                swampElement = lst[element-1]
                lst[element-1] = lst[element]
                lst[element] = swampElement
                flag = True
        if flag == False:
            break
    return lst

if __name__ == '__main__':
    numb_list = [3,1,5,8,0,76,-34,456,9876,8,29]
    print(Reverse_Bubble_Sort(numb_list))


'''
Output:
[9876, 456, 76, 29, 8, 8, 5, 3, 1, 0, -34]
'''
