def isPossible(self, nums: list[int]) -> bool:
    c1 = c2 = c3 = 0
    i = 0

    while i < len(nums):
        j = i
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        count = j - i

        if i == 0 or nums[i] != nums[i - 1] + 1:
            if c1 or c2:
                return False
            c1, c2, c3 = count, 0, 0
        else:
            if c1 + c2 > count:
                return False
            c1, c2, c3 = max(0, count - (c1 + c2 + c3)), c1, c2 + min(c3, count - c1 - c2)
        i = j

    return c1 == c2 == 0