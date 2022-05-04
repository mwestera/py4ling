import re

print(re.findall(r'[A-Z]', 'Abc ABc abC abc'))

print(re.findall(r'[A-Za-z]+', 'Abc ABc abC abc'))

print(re.findall(r'[^A-Z]+', 'Abc ABc abC abc'))

print(re.findall(r'an?', 'A woman bought a bank and an acre of land.'))

print(re.findall(r'\d+\d', '8+12 = 6+14'))

print(sorted([4, 3, 2, 3, 1]))

print(sorted([4, 3, 2, 3, 1], key=lambda x: -x))

print(sorted('banana'))

points = {'a': 10, 'b': 5, 'n': 100}
print(sorted('banana', key=lambda x: points[x]))

print(sorted(points.keys(), key=lambda x: points[x]))

print(sorted('this is a sentence'.split(), key=len))

def mystery_function(s):
    count = 0
    for c in s:
        if c.lower() not in 'aeiou':
            count += 1
    return count / len(s)

print(sorted('huh oooh hahaha'.split(), key=mystery_function))
