my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list, type(my_list))

ascendent_list = my_list.copy()
ascendent_list.sort(reverse=False)
print(ascendent_list)

descendent_list = my_list.copy()
descendent_list.sort(reverse=True)
print(descendent_list)

even_list = ascendent_list
my_sliced_even_list = even_list[::-2]
print('numere_pare = ', my_sliced_even_list)

odd_list = ascendent_list
my_sliced_odd_list = odd_list[::2]
print('numere_impare = ', my_sliced_odd_list)


int_list = my_sliced_odd_list.copy()
print(len(int_list))
int_list_0 = int_list[0] % 3 == 0
print('primul numar este multiplu de 3 = ', int_list_0)
int_list_1 = int_list[1] % 3 == 0
print('al doilea numar este multiplu de 3 = ', int_list_1)
int_list_2 = int_list[2] % 3 == 0
print('al treilea numar este multiplu de 3 = ', int_list_2)
int_list_3 = int_list[3] % 3 == 0
print('al patrulea numar este multiplu de 3 = ', int_list_3)
int_list_4 = int_list[4] % 3 == 0
print('al cincilea numar este multiplu de 3 = ', int_list_4)

new_list_1 = int_list[1]
new_list_2 = int_list[4]
print(new_list_1, new_list_2)

print(my_list)




