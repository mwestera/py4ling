import random


already_answered = {}
while True:
    q = input('Enter a yes/no question (or blank to quit)')
    if not q:   # if q == ''    if len(q) == 0
        print('Bye!')
        break
    if not q.endswith('?'):
        continue
    if q not in already_answered:
        answer = random.choice(['yes', 'no'])
        already_answered[q] = answer
    else:
        answer = already_answered[q]
    print(answer)


