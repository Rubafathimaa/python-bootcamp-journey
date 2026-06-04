def evenfilter(lst):
    return [num for num in lst if num % 2 == 0]
list1 = [5, 2, 7, 9, 4, 6]
evens = evenfilter(list1)
print(evens)