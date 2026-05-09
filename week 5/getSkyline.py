def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
    events = []
    for left, right, height in buildings:
        events.append((left, -height))
        events.append((right, height))
    events.sort(key=lambda x: (x[0], x[1]))

    result = []
    heights = [0]
    prev_max_height = 0

    for x, h in events:
        if h < 0:
            heights.append(-h)
        else:
            heights.remove(h)

        current_max_height = max(heights)
        if current_max_height != prev_max_height:
            result.append([x, current_max_height])
            prev_max_height = current_max_height

    return result