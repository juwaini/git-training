# def function_name(a,b,c):
#     <body of function>
#     return <return_value>

def add(a, b):
    total = a + b
    return total

def total(*args, **kwargs):
    ...
nama = 'Jerry'
umur = 20

total(nama = nama, umur = umur)
total(1,2,3,4,5)
total('hello', 'world')

add_a = add(1, 2)
add_b = add('hello', 'reen')
add_c = add(1.0, 3)
#add_d = add(3, 'hello')

print(add_a,add_b,add_c)
#print(add_d)