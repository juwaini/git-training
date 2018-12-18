list_a = [1,3,5,7,9]
list_b = list()
list_c = [1,2,3,4,5]

#cara nak print list

#cara 1
print(list_a)
print(list_b)
#cara 2
print(len(list_a))
print(len(list_b))

#condition (if statement)
if 1 in list_a:
    print('Ada')
else:
    print('tiada')

#list comprehension
list_d = [i*i for i in list_c]
print (list_d)

#list operation

empty_list = []

#list akan bertambah dibelakang
empty_list.append('a')
empty_list.append('b')
print(empty_list)

#tambah list sedia ada dengan list lain
list_extend = []
list_extend.extend(list_d)
print(list_extend)

list_extend2 = list_a
list_extend2.extend(list_extend)
print(list_extend2)

list_c.extend(list_d)
print(list_c)