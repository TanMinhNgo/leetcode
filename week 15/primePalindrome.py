
def primePalindrome(self, n: int) -> int:
    def is_prime(x):
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True
    
    if 8 <= n <= 11:
        return 11
    for x in range(1, 10**5):
        s = str(x)
        y = int(s + s[-2::-1])
        if y >= n and is_prime(y):
            return y
    return -1