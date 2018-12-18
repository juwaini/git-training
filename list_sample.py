list_a = ['banana', 'kiwi']
list_b = list()
list_c = [1, 2, 3, 4, 5]

# Check List Empty or Not
print(len(list_a))

if list_a == 0:
    print("Kosong")
else:
    print("Ada Data")


if 'banana' in list_a:
    print("Bananananaa")
else:
    print("laaaa")


list_d = [x*2 for x in list_c]
print(list_d)

empty_list = []
empty_list.append('a')
empty_list.append('b')
empty_list.append('c')

print(empty_list)

list_a.extend(list_c)

print(list_a)

