def postfix_to_infex(s):
    s = s.split()
    stack = []
    try:
        for i in s:
            if i.isdigit():
                stack.append(int(i))
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(f"({b} + {a})")
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(f"({b} - {a})")
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(f"({b} * {a})")
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(f"({b} / {a})")
            else:
                return "Error, uncorrect symbol"
    except IndexError:
        return "Error, uncorrect data"
    if len(stack) != 1:
        return "Error, uncorrect data"
    return " ".join(stack)

def postfix_eval(s):
    s = s.split()
    stack = []
    try:
        for i in s:
            if i.isdigit():
                stack.append(int(i))
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(b / a)
            else:
                return "Error, uncorrect symbol"
    except IndexError:
        return "Error, uncorrect data"
    if len(stack) != 1:
        return "Error, uncorrect data"
    return stack[0]

def postfix_to_prefix(s):
    s = s.split()
    stack = []
    try:
        for i in s:
            if i in "*-+/":
                a = stack.pop()
                b = stack.pop()
                stack.append(i + b + a)
            elif i.isdigit():
                stack.append(i)
            else:
                return "Error, uncorrect symbol"
    except IndexError:
        return "Error, uncorrect data"
    if len(stack) != 1:
        return "Error, uncorrect data"
    return " ".join(list(stack[0]))

def prefix_to_postfix(s):
    s = s.split()
    stack = []
    try:
        for i in s[::-1]:
            if i in "*-+/":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b + i)
            elif i.isdigit():
                stack.append(i)
            else:
                return "Error, uncorrect symbol"
    except IndexError:
        return "Error, uncorrect data"
    if len(stack) != 1:
        return "Error, uncorrect data"
    return " ".join(list(stack[0]))

def prefix_to_infex(s):
    try:
        return postfix_to_infex(prefix_to_postfix(s))
    except Exception:
        return prefix_to_postfix(s)

def prefix_eval(s):
    try:
        return postfix_eval(prefix_to_postfix(s))
    except Exception:
        return prefix_to_postfix(s)

def infex_to_postfix(s):
    func = {'+': 2, '-': 2, '*': 1, "/": 1}
    stack = []
    q = []
    for i in s:
        if i.isdigit():
            q.append(i)
        elif i in func:
            if stack == [] or stack[-1] == '(':
                stack.append(i)
            elif func[i] < func[stack[-1]]:
                stack.append(i)
            else:
                while stack != [] and stack[-1] != '(' and func[stack[-1]] < func[i]:
                    q.append(stack.pop())
                stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            j = len(stack) - 1
            while stack[j] != '(':
                q.append(stack.pop())
                j -= 1
            del stack[-1]
    if stack != []:
        for i in stack:
            q.append(i)
    return ' '.join(q)

def infex_to_prefix(s):
    try:
        return postfix_to_prefix(infex_to_postfix(s))
    except Exception:
        return infex_to_postfix(s)

def infex_eval(s):
    try:
        return postfix_eval(infex_to_postfix(s))
    except Exception:
        return infex_to_postfix(s)

###########################
#*************************#
###########################


def postfix_to_all(s):
    print(f"\n??????????????????:")
    print("  1. ??????????????:", postfix_to_prefix(s))
    print("  2. ????????????:", postfix_to_infex(s))
    print("  3. ????????????????:", postfix_eval(s))

def prefix_to_all(s):
    print(f"\n??????????????????:")
    print("  1. ????????????????:", prefix_to_postfix(s))
    print("  2. ????????????:", prefix_to_infex(s))
    print("  3. ????????????????:", prefix_eval(s))

def infex_to_all(s):
    print(f"\n??????????????????:")
    print("  1. ??????????????:", infex_to_prefix(s))
    print("  2. ????????????????:", infex_to_postfix(s))
    print("  3. ????????????????:", infex_eval(s))

def auto_to_all(s):
    if s[0] in "-*+/":
        return "prefix"
    elif s[-1] in "-*+/":
        return "postfix"
    else:
        return "infex"

def question(data):
    keys = list(data.keys())
    print("???????????????? ??????????:")
    for i in keys:
        print(f"  {i}: {data[i]}")
    s = input(">>> ")
    while s not in keys:
        print("???? ?????????????? ???????????????? ??????????")
        s = input(">>> ")
    return s
