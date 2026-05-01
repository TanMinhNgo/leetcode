def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
    maxh = 0
    maxw = 0
    currw = 0
    currh = 0
    horizontalCuts.append(h)
    verticalCuts.append(w)
    horizontalCuts.sort()
    verticalCuts.sort()

    for h in horizontalCuts:
        if (h - currh) > maxh:
            maxh = h - currh
        currh = h

    for v in verticalCuts:
        if (v - currw) > maxw:
            maxw = v - currw
        currw = v
        
    return ( maxh * maxw ) % (10**9 + 7)