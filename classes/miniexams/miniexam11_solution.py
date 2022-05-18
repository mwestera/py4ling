
results = [
    list(enumerate('abc')),
    list(zip(range(5), 'abc')),
    list(enumerate(range(3))),
    list(zip(range(2), range(3))),
    list(zip('abc', 'def')),
    list(zip(range(0, 6, 2), range(1, 7, 2))),
    ]

print(*results, sep='\n')


number = 2
print(not any(number % n == 0 for n in range(2, number)))

# equivalent:  all(number % n != 0 for n in range(2, number))