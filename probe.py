from random import randint
list=[]
for i in range(10):
    list.append(i)
    print(i)
list_del = [8,5,3,9]
print(list_del)
list_del.sort()
print(list_del)
list_del.reverse()
print(list_del)
print(list)
for i in list_del:
    list.pop(i)
print(list)