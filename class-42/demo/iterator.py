def gen():
    for i in range(10):
        yield i

num_gen = gen()
# print(num_gen)
# print(next(num_gen))
try:
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))
    print(next(num_gen))

except StopIteration:
    print('All Done')
