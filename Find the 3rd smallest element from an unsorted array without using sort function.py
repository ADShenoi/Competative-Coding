lst = [char for char in map(int, input().split())]
lst.remove(min(lst))
lst.remove(min(lst))
print(min(lst))