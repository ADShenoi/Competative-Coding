def find_pair(lst):
    for i in range(0,len(lst)):
        for j in range(i+1, len(lst)):
            if(lst[i]+lst[j]) in lst:
                l.append((lst[i],lst[j]))


lst = [char for char in map(int, input().split())]
l = []
find_pair(lst)
print(l)