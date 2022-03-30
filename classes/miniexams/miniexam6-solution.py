def gossip(subject, object='themselves', verb='love'):
    print(f'{subject} {verb}s {object}')

gossip('Alf', 'Beth')
print('Alf', 'Beth', 'love')
gossip('Alf', 'Beth', 'hate')
gossip('Sue', verb='know')
gossip('Alf', 'hate')
gossip(subject='John', verb='love')
print(gossip('Alf', 'Beth'))

# equivalent to:
# a = gossip('Alf', 'Beth')
# print(a)

# gossip(object='Beth', verb='know')    # error
gossip('Alf', 'himself', verb='envy')
# gossip(subject='Zoe', 'Xyla', 'like') # error
gossip(subject='Dale', object='Ebba')
gossip(verb='see', subject='Alf', object='Beth')
# gossip('Bert', 'see', subject='Ernie')    # error

# Bonus:
# gossip('Bert', 'Ernie', verb='see', verb='love')  # error

