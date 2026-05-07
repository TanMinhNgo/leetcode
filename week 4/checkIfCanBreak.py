def checkIfCanBreak(self, s1: str, s2: str) -> bool:
    s1_sorted, s2_sorted = sorted(s1), sorted(s2)
    
    can_s1_break, can_s2_break = True, True
    for i in range(len(s1)):
        if s1_sorted[i] < s2_sorted[i]:
            can_s1_break = False
        if s2_sorted[i] < s1_sorted[i]:
            can_s2_break = False

    return can_s1_break or can_s2_break