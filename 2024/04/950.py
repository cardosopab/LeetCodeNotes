# 950. Reveal Cards In Increasing Order
# Medium
# You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].
# You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.
# You will do the following steps repeatedly until all cards are revealed:
# 1. Take the top card of the deck, reveal it, and take it out of the deck.
# 2. If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
# 3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.
# Note that the first entry in the answer is considered to be the top of the deck.


from collections import deque


def deckRevealedIncreasing(deck):
    N = len(deck)
    deck.sort()
    res = [0] * N
    q = deque(range(N))

    for n in deck:
        i = q.popleft()
        res[i] = n

        if q:
            q.append(q.popleft())

    return res


# Example 1:
deck = [17, 13, 11, 2, 3, 5, 7]
ans = [2, 13, 3, 11, 5, 17, 7]
print("Pass" if deckRevealedIncreasing(deck) == ans else "Fail")
# Explanation:
# We get the deck in the order[17, 13, 11, 2, 3, 5, 7](this order does not matter), and reorder it.
# After reordering, the deck starts as [2, 13, 3, 11, 5, 17, 7], where 2 is the top of the deck.
# We reveal 2, and move 13 to the bottom.  The deck is now[3, 11, 5, 17, 7, 13].
# We reveal 3, and move 11 to the bottom.  The deck is now[5, 17, 7, 13, 11].
# We reveal 5, and move 17 to the bottom.  The deck is now[7, 13, 11, 17].
# We reveal 7, and move 13 to the bottom.  The deck is now[11, 17, 13].
# We reveal 11, and move 17 to the bottom.  The deck is now[13, 17].
# We reveal 13, and move 17 to the bottom.  The deck is now[17].
# We reveal 17.
# Since all the cards revealed are in increasing order, the answer is correct.
# Example 2:
deck = [1, 1000]
ans = [1, 1000]
print("Pass" if deckRevealedIncreasing(deck) == ans else "Fail")
# Constraints:
# 1 <= deck.length <= 1000
# 1 <= deck[i] <= 106
# All the values of deck are unique.


def deckRevealedIncreasing(deck):
    N = len(deck)
    deck.sort()
    skip = False
    res_i = 0
    deck_i = 0
    res = [0] * N

    while deck_i < N:
        if res[res_i] == 0:

            if not skip:
                res[res_i] = deck[deck_i]
                deck_i += 1

            skip = not skip

        res_i = (res_i + 1) % N

    return res


# Example 1:
deck = [17, 13, 11, 2, 3, 5, 7]
ans = [2, 13, 3, 11, 5, 17, 7]
print("Pass" if deckRevealedIncreasing(deck) == ans else "Fail")
# Example 2:
deck = [1, 1000]
ans = [1, 1000]
print("Pass" if deckRevealedIncreasing(deck) == ans else "Fail")
