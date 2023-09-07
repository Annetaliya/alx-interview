#!/usr/bin/python3
''' solution to prime game'''


def isWinner(x, nums):
    def isPrime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def canWin(n):
        if n <= 1:
            return False
        if dp[n] != -1:
            return dp[n]
        result = False
        for i in range(2, n + 1):
            if isPrime(i):
                if not canWin(n - i):
                    result = True
                    break
        dp[n] = result
        return result

    winner_count = {"Maria": 0, "Ben": 0}

    for n in nums:
        dp = [-1] * (n + 1)
        if canWin(n):
            winner_count["Maria"] += 1
        else:
            winner_count["Ben"] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Ben"] > winner_count["Maria"]:
        return "Ben"
    else:
        return None
