#tuple is immutable

tuple_a = ('a','a','b','c','a')
tuple_b = tuple()

print(bool(tuple_a))
print(bool(tuple_b))

tuple_c = (1,2,3)
tuple_d = 1,

print(tuple_c)
print(tuple_d)

#tuple operation

print(tuple_a.count('a'))
print(tuple_c.index(1))
print(tuple_a[0])