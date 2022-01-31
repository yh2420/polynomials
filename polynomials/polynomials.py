from numbers import Number


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

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):
        
        return self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial): # other 是Polynomial时

            common = min(self.degree(), other.degree()) + 1 # 两者相加both contribute 的 term 个数
            coefs = tuple(a + b for a, b in zip(self.coefficients, 
                                                other.coefficients))  
            # zip(list1,list2) list1，2中的元素一一对应地相加，ith+ith作为zip输出的ith，以len()小的相加对象为准
            coefs += self.coefficients[common:] + other.coefficients[common:] 
            # [common:]从common（含）到结束的所有index；tuple相加是在tuple原来基础上在后面append；self和other哪一个degree更高这里就加上哪个的coefs
            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,) # tuple(,) length-1 tuple 有逗号
                            + self.coefficients[1:])
        
        else:
            return NotImplemented

    def __radd__(self, other): # other + self
        return self + other