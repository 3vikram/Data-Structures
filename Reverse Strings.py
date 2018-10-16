def Reversing(str):
    first_character = 0
    last_character = len(str)-1
    final_character_list = []

    for string in str:
        final_character_list.append(string)

    while(True):
        if first_character != last_character and last_character > first_character:
            temp_memory = final_character_list[first_character]
            final_character_list[first_character] = final_character_list[last_character]
            final_character_list[last_character] = temp_memory
            first_character += 1
            last_character -= 1
        else:
            break

    reversed_string = ''
    for rString in final_character_list:
        reversed_string += rString
    return reversed_string


if __name__=='__main__':
    string = "trivikram"
    print(Reversing(string))


'''
Output:
markivirt
'''
