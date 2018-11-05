def Reversing(lst):
    list_length = len(lst)-1
    first_index = 0
    last_index = list_length
    while(True):
        if first_index != last_index and last_index > first_index:
            temp_memory = lst[first_index]
            lst[first_index] = lst[last_index]
            lst[last_index] = temp_memory
            first_index += 1
            last_index -= 1
        else:
            break
    return lst

if __name__=='__main__':
    numbers = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
    strings = ['a','b','c','d']
    print(Reversing(numbers))
    print(Reversing(strings))


'''
Output:
[150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
['d', 'c', 'b', 'a']
'''
