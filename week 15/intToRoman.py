def intToRoman(self, num: int) -> str:
    reference = [(1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (8, 'VIII'),
                (7, 'VII'),
                (6, 'VI'),
                (5, 'V'),
                (4, 'IV'),
                (3, 'III'),
                (2, 'II'),
                (1, 'I')]
                

    curr = ''
    for i in reference:
        if num <0:
            break
            
        if num>=i[0]:
            count = num // i[0]
            num -= i[0] * count
            curr += i[1] * count
        
    return curr