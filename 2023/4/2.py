from sys import stdin


# def count_cards(cards: list[int], i: int):
#     global answer
#     answer += cards[i]

#     for j in range(i + 1, min(i + cards[i] + 1, len(cards))):
#         count_cards(cards, j)


cards = []
for line in stdin:
    _, numbers = line.split(':')
    winning, total = numbers.split('|')
    winning = map(int, winning.split())
    winning = set(winning)
    total = map(int, total.split())
    total = set(total)

    matches = len(total.intersection(winning))
    cards.append(matches)

answer = [1] * len(cards)
for i in range(0, len(cards)):
    for j in range(i + 1, min(i + cards[i] + 1, len(cards))):
        answer[j] += answer[i]

print(sum(answer))
