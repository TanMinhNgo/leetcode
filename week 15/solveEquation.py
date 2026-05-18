def solveEquation(self, equation: str) -> str:
    def parse(side: str):
        x_coef = 0
        const = 0
        for term in side.replace('-', '+-').split('+'):
            if not term:
                continue
            if term.endswith('x'):
                coef = term[:-1]
                if coef in ('', '+'):
                    x_coef += 1
                elif coef == '-':
                    x_coef -= 1
                else:
                    x_coef += int(coef)
            else:
                const += int(term)
        return x_coef, const

    left, right = equation.split('=')
    x_count = parse(left)[0] - parse(right)[0]
    num_count = parse(left)[1] - parse(right)[1]
    if x_count == 0:
        return 'Infinite solutions' if num_count == 0 else 'No solution'
    return 'x=' + str(-num_count // x_count)