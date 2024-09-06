def canPlaceFlowers(flowerbed, n):
    padded_flowerbed = [0] + flowerbed + [0]  # Add padding to avoid boundary checks
    count = 0
    for i in range(1, len(padded_flowerbed) - 1):
        if padded_flowerbed[i - 1] == 0 and padded_flowerbed[i] == 0 and padded_flowerbed[i + 1] == 0:
            padded_flowerbed[i] = 1
            count += 1
            if count >= n:
                return True
    return count >= n

# Example usage
print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
