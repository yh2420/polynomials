from calendar import c
from this import d


class Polynomial:
    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):

        coefs = self.coefficients # 因为每次写.coefficients太长了，简写成coefs
        terms = [] # 用list，因为mutable，可以指定位置定义内容，添加element

        if coefs[0]: # 默认不等于=!0即True
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x") # “{}”花括号里的内容直接变string

        terms +=[f"{''if c == 1 else c}x^{d}"
                for d, c in enumerate(coefs[2:], start=2) if c] # 当c=!0时
        
        return " + ".join(reversed(terms)) or "0"
