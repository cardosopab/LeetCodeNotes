# 2073. Time Needed to Buy Tickets
# Easy
# There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.
# You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].
# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.
# Return the time taken for the person at position k (0-indexed) to finish buying tickets.


def timeRequiredToBuy(tickets, k):
    timer, i = 0, 0

    while tickets[k] > 0:
        if tickets[i] > 0:
            tickets[i] -= 1
            timer += 1
        i = (i + 1) % len(tickets)

    # print(timer)
    return timer


# Example 1:
tickets = [2, 3, 2]
k = 2
ans = 6
print("Pass" if timeRequiredToBuy(tickets, k) == ans else "Fail")
# Explanation:
# - In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
# - In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
# The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
# Example 2:
tickets = [5, 1, 1, 1]
k = 0
ans = 8
print("Pass" if timeRequiredToBuy(tickets, k) == ans else "Fail")
# Explanation:
# - In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
# - In the next 4 passes, only the person in position 0 is buying tickets.
# The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.
# Constraints:
# n == tickets.length
# 1 <= n <= 100
# 1 <= tickets[i] <= 100


def timeRequiredToBuy(tickets, k):
    N = len(tickets)

    timer = tickets[k]

    for i in range(N):
        if i < k:
            timer += min(tickets[i], tickets[k])
        elif i > k:
            timer += min(tickets[i], tickets[k] - 1)
    return timer


# Example 1:
tickets = [2, 3, 2]
k = 2
ans = 6
print("Pass" if timeRequiredToBuy(tickets, k) == ans else "Fail")
# Example 2:
tickets = [5, 1, 1, 1]
k = 0
ans = 8
print("Pass" if timeRequiredToBuy(tickets, k) == ans else "Fail")
