set_a = set()
set_b = {'a','e','i','o','u'}
set_c = {'a', 'b','c','d','e'}


set_b.add('a')

intersect = set_b.intersection(set_c)

print(intersect)
print(set_b)