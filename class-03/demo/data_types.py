# Tuple
# Not mutable
my_list = [1, 2, 2, 3, 3, 4]
my_tuple = (1, 2, 2, 3, 3, 4)
my_list.append(5)
# print(my_list)

my_tuple = list(my_tuple)
my_tuple.append(5)
my_tuple = tuple(my_tuple)
# print(my_tuple)

my_tuple = (1, 2, 2, 3, 3, 4, 5, 6)
print(my_tuple[0])
# set will only allow 1 unique item

my_set = set(my_tuple)
# print(my_set) # -> (1, 2, 3, 4, 5, 6)

for item, index in enumerate(my_tuple):
    # print(item)
    # print(index)
    pass


new_tuple = (1,)

print(type(new_tuple))

my_object ={
    "tuple1":(0, 1, 2, 3),
    "tuple2":(0, 1, 2, 3)
}

print(my_set)
my_set.pop()
print(my_set)

if 2 in my_set:
    print('it is here')

for num in my_set:
    if num == 2:
        print('it is still here')

