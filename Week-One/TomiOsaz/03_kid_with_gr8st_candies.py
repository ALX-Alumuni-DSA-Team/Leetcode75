
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]

# Trial run 1
print(kidsWithCandies([6, 2, 3, 5, 8], 6))  # Output: [True, True, True, True, True]

# Trial run 2
print(kidsWithCandies([2, 8, 4, 1, 6], 9))  # Output: [True, True, True, True, True]

# Trial run 3
print(kidsWithCandies([4, 5, 5, 9, 7], 3))  # Output: [False, False, False, True, True]
