class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        index = 0
        init_count = flowerbed.count(1)
        len_ = len(flowerbed)
        for cycle in range(n):
            while index < len_:
                if flowerbed[index] == 0:
                    if (((index > 0) and index < len_-1 and flowerbed[index-1] == 0 and flowerbed[index+1] == 0) or
                            len_-1 == index and flowerbed[index-1] == 0) or \
                            (index == 0 and flowerbed[index+1] == 0):
                        flowerbed[index] = 1
                        break
                index += 1
        return True if init_count + n == flowerbed.count(1) else False
