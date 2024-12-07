class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low = 1
        high = x
        result = 0
        while low <= high:
            mid = (low + high) // 2
            y = mid * mid
            if y == x:
                return mid
            elif y < x:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result

    def sx(self, x):
        l = 0
        while True:
            if l * l == x:
                return l
            elif l * l < x:
                l += 1
            else:
                return l - 1

if __name__ == '__main__':
    t = Solution().mySqrt(2)
    print(t)