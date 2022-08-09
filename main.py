import sort_algorithms as sa


l: list = [92, 15, 4, 10, 500, 3, 23, 45, 510, 239, 57, -45, 105, -1, 222, 486, 0, 199, 99]

l_sorted: list = sa.bubble_sort(data=l.copy())
print('before bubble sort: ', l, end='\n')
print('after bubble sort: ', l_sorted, end='\n')

l_sorted: list = sa.quick_sort(data=l.copy())
print('before quick sort: ', l, end='\n')
print('after quick sort: ', l_sorted, end='\n')
