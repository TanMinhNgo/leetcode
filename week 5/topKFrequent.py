def topKFrequent(self, words: list[str], k: int) -> list[str]:
    words.sort()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    freq = [[] for i in range(len(words) + 1)]
    for word, c in count.items():
        freq[c].append(word)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for word in freq[i]:
            res.append(word)
            if len(res) == k:
                return res