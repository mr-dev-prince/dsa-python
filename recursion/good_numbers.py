class Solution:
    # binary exponentiation
    def findPower(self, a, b):
        if b == 0 : return 1

        half = self.findPower(a, b//2)
        result = (half * half) % self.M

        if b % 2 == 1:
            result = (result * a) % self.M

        return result

    def countGoodNumbers(self, n: int) -> int:
        self.M = 1000000007
        # number of even places in n digit number = (n+1) // 2 --> m
        # number of odd places in n digit number = n // 2 --> n
        # number of possible numbers =( N^m * N^n)
        return (self.findPower(5, (n+1)//2) * self.findPower(4, n//2)) % self.M