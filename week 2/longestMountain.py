def longestMountain(self, arr: list[int]) -> int:
    longest = 0
    n = len(arr)

    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            left = i - 1
            right = i + 1

            while left >= 0 and arr[left] < arr[left + 1]:
                left -= 1

            while right < n and arr[right] < arr[right - 1]:
                right += 1

            longest = max(longest, right - left - 1)

    return longest