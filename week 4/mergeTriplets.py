def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
    find_a, find_b, find_c = False, False, False
    a_target, b_target, c_target = target

    for triplet in triplets:
        a, b, c = triplet
        if a == a_target and b <= b_target and c <= c_target:
            find_a = True
        if a <= a_target and b == b_target and c <= c_target:
            find_b = True
        if a <= a_target and b <= b_target and c == c_target:
            find_c = True
        
        if find_a and find_b and find_c:
            return True
    
    return False