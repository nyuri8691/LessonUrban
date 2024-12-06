my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
cicle_list = []
while i < len(my_list):
    temp_num = my_list[i]
    if temp_num > 0:
        cicle_list.append(temp_num)
        print(temp_num)
    elif temp_num < 0:
        break
    i += 1
