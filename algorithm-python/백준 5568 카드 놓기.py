from itertools import permutations

n = int(input())
k = int(input())
cards = []
for _ in range(n):
    cards.append(input())
cards = list(permutations(cards, k))


sub = 0
cards_combi = set([int("".join(card)) for card in cards])
print(len(cards_combi))
