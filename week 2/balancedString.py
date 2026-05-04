def balancedString(self, s: str) -> int:
    n = len(s)
    target = n // 4
    freq = {c: 0 for c in "QWER"}
    for c in s:
        freq[c] += 1

    if all(freq[c] == target for c in "QWER"):
        return 0

    need = {c: max(0, freq[c] - target) for c in "QWER"}

    left = 0
    ans = n
    for right in range(n):
        cr = s[right]
        if cr in need:
            need[cr] -= 1

        while left <= right and all(need[c] <= 0 for c in "QWER"):
            ans = min(ans, right - left + 1)
            cl = s[left]
            if cl in need:
                need[cl] += 1
            left += 1

    return ans