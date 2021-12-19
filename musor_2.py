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
    print(f"\nРезультат:")
    print("  1. Префикс:", postfix_to_prefix(s))
    print("  2. Инфикс:", postfix_to_infex(s))
    print("  3. Значение:", postfix_eval(s))

def prefix_to_all(s):
    print(f"\nРезультат:")
    print("  1. Постфикс:", prefix_to_postfix(s))
    print("  2. Инфикс:", prefix_to_infex(s))
    print("  3. Значение:", prefix_eval(s))

def infex_to_all(s):
    print(f"\nРезультат:")
    print("  1. Префикс:", infex_to_prefix(s))
    print("  2. Постфикс:", infex_to_postfix(s))
    print("  3. Значение:", infex_eval(s))

def auto_to_all(s):
    if s[0] in "-*+/":
        return "prefix"
    elif s[-1] in "-*+/":
        return "postfix"
    else:
        return "infex"

def question(data):
    keys = list(data.keys())
    print("Выберите пункт:")
    for i in keys:
        print(f"  {i}: {data[i]}")
    s = input(">>> ")
    while s not in keys:
        print("Вы выбрали неверный пункт")
        s = input(">>> ")
    return s

def interface():
    print("*********************************************")
    print("*    Вас приветсвует калькулятор ZAvrCalc   *")
    print("*********************************************")
    print("* Чтобы выйти из программы нажмите Ctrl + C *")
    print("*********************************************")
    print()
    while True:
        ans = question({"1": "Посчитать из определённого вида выражения", "2": "Определить вид выражения"})
        if ans == "1":
            ans = question({"1": "Из инфикса", "2": "Из постфикса", "3": "Из префикса"})
            if ans == "1":
                ans = question({"1": "В префикс", "2": "В постфикс", "3": "Посчитать", "4": "Всё вместе"})
                if ans == "1":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {infex_to_prefix(s)}")
                elif ans == "2":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {infex_to_postfix(s)}")
                elif ans == "3":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {infex_eval(s)}")
                elif ans == "4":
                    s = input("Введите выражение >>> ")
                    infex_to_all(s)
            elif ans == "2":
                ans = question({"1": "В префикс", "2": "В инфикс", "3": "Посчитать", "4": "Всё вместе"})
                if ans == "1":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {postfix_to_prefix(s)}")
                elif ans == "2":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {postfix_to_infex(s)}")
                elif ans == "3":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {postfix_eval(s)}")
                elif ans == "4":
                    s = input("Введите выражение >>> ")
                    postfix_to_all(s)
            elif ans == "3":
                ans = question({"1": "В постфикс", "2": "В инфикс", "3": "Посчитать", "4": "Всё вместе"})
                if ans == "1":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {prefix_to_postfix(s)}")
                elif ans == "2":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {prefix_to_infex(s)}")
                elif ans == "3":
                    s = input("Введите выражение >>> ")
                    print(f"\nРезультат: {prefix_eval(s)}")
                elif ans == "4":
                    s = input("Введите выражение >>> ")
                    prefix_to_all(s)
        elif ans == "2":
            s = input("Введите выражение >>> ")
            ans = auto_to_all(s)
            if ans == "prefix": f = "Префикс"
            if ans == "postfix": f = "Постфикс"
            if ans == "infex": f = "Инфикс"
            print(f"\nРезультат: {f}")
            sl_1 = {0: "Префикс", 1: "Постфикс", 2: "Инфикс", 3: "Значение"}
            sl = {0: "_to_prefix", 1: "_to_postfix", 2: "_to_infex", 3: "_eval"}
            for i in range(4):
                try:
                    print(f"  {i}. {sl_1[i]}: {globals()[ans + sl[i]](s)}")
                except Exception:
                    pass
        print()
        print("*******************************************")
        print()

if __name__ == "__main__":
    try:
        interface()
    except KeyboardInterrupt:
        print()
        print("*********************************************")
        print("*   Спасибо, что воспользовались ZAvrCalc   *")
        print("*********************************************")