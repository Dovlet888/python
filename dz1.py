def odd_nums(n):
    for i in range(1, n+1, 2):
        yield i


odd_to_8 = odd_nums(8)
print(next(odd_to_8))
print(next(odd_to_8))
print(next(odd_to_8))
print(next(odd_to_8))
print(next(odd_to_8))
print(next(odd_to_8))
print(next(odd_to_8))
print(next(odd_to_8))
