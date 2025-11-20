def i_number(val):
    i = input(val)
    try:
        return int(i)
    except ValueError:
        try:
            return float(i)
        except ValueError:
            raise
try:
    x = i_number("Введите число:\n")
    y = i_number("Введите число:\n")
    op = input("Введите нужный вам оператор:\nПримеры:+,-,*,/,//,%,**\n")
    if op == "+":
        r = x + y
    elif op == "-":
        r = x - y
    elif op == "*":
        r = x * y
    elif op == "/":
        r = x / y
    elif op == "//":
        r = x // y
    elif op == "%":
        r = x % y
    elif op == "**":
        r = x ** y
    else:
        None
    print(r)
except ZeroDivisionError:
    print("На ноль делить нельзя")
except ValueError:
    print("Ошбика в значений , используйте числа")