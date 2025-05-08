from typing import List
"""
    Dynamic Programing problems 
"""

def fibonacci(n):
    """
    Bottom up
    """
    if n <= 1:
        return n
    memo = [0]*(n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
        memo[i] = memo[i-2] + memo[i-1]
    return memo[n]

def coinChange(coins: List[int], amount: int):
    """
    Given coin denominations c_1, c_2, ..., c_n and a target amount V, find the minimum number of coins required to make exactly V.
    """
    if amount == 0:
        return 0
    memo = [amount + 1] * (amount + 1)
    memo[0]=[0]
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                memo[a] = min(memo[a], 1 + memo[a-c])
    return memo[amount] if memo[amount] != amount + 1 else -1

def unboundedKnapsack(amount: int, coins: list[int]):
    """
    In the unbounded knapsack, you can take as many copies of each item as you want.
    Unlike the 0/1 knapsack, where you can only take one of each item.
    """
    memo = [0] * (amount + 1)
    memo[0] = 1
    N = len(coins)
    for i in range(N-1, -1, -1):
        next = [0] * (amount + 1)
        next[0] = 1
        for a in range(1, amount + 1):
            next[a] = memo[a]
            if a - coins[i] >= 0:
                next[a] += next[a-coins[i]]
        memo = next
    return memo[amount]

def knapsack_01(weight: list[int], value: list[int], capacity: int):
    """
    You can take at most one of each item — either you take it (1) or you don't (0) — hence the name "0-1".
    """
    N = len(weight)
    maxValue = [[0] * (capacity + 1) for _ in range(N+1)]
    for i in range(1, N + 1):
        for c in range(1, capacity + 1):
            if weight[i-1] <= c:
                maxValue[i][c] = max(
                    maxValue[i-1][c],
                    value[i-1] + maxValue[i-1][c-weight[i-1]]
                )
            else:
                maxValue[i][c] = maxValue[i-1][c]
    return maxValue[N][c]

def editDistance(word1: str, word2: str):
    """
    Hate this but love it, typical 2d dp problem
    Given two strings word1 and word2, return the min number of operations required to convert word1 to word2 
    """
    # create 2d array
    cashe = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]
    # initialize row
    for j in range(len(word2)+1):
        cashe[len(word1)][j] = len(word2) - j
    # initialize col 
    for i in range(len(word1)+1):
        cashe[i][len(word2)] = len(word1) - i
    # bottom up sol
    for i in range(len(word1)-1,-1,-1):
        for j in range(len(word2)-1,-1,-1):
            if word1[i] == word2[j]:
                cashe[i][j] == cashe[i+1][j+1]
            else:
                cashe[i][j] = 1 + min(cashe[i+1][j], cashe[i][j+1], cashe[i+1][j+1])
    return cashe[0][0]