def IsEmpty(L):
    """IsEmpty(L) benar jika list kosong"""
    return L == [] or L == ""


def Operand0(S):
    return S[0]


def Operand1(S):
    return S[1]


def Operand2(S):
    return S[2]


def EvaluateExpression(S):
    if IsEmpty(S):
        return []
    if Operand0(S) == "+":
        return Operand1(S) + Operand2(S)
    if Operand0(S) == "-":
        return Operand1(S) - Operand2(S)
    if Operand0(S) == "*":
        return Operand1(S) * Operand2(S)
    if Operand0(S) == "/":
        return Operand1(S) / Operand2(S)


print(eval(input()))
