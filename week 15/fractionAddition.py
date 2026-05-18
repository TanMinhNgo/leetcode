def fractionAddition(self, expression: str) -> str:
    total_num,total_den=0,1
    for num,den in re.findall(r'([-+]?\d+)/(\d+)',expression):
        n,d = int(num),int(den)
        total_num=total_num*d+n*total_den
        total_den*= d

    gcd = math.gcd(total_num,total_den)
    total_num = total_num//gcd
    total_den = total_den//gcd

    return f"{total_num}/{total_den}"