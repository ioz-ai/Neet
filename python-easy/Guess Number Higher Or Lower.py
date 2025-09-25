# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# 0: your guess is equal to the number I picked (i.e. num == pick).
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# Return the number that I picked.

class Solution:
    def guessNumber(self, n: int) -> int:
        # binary search
        l = 1
        r = n

        while l <= r:
            mid = l + (r - l) // 2
            res = guess(mid)

            if res == 0:
                return mid
            if res == 1:
                l = mid+1
            else:
                r = mid-1
            mid = l + (r - l) // 2
        return -1