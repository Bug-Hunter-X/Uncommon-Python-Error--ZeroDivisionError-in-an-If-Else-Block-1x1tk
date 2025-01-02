def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 1
    except ZeroDivisionError:
        return "Error: Division by zero"

result = function_with_uncommon_error(0)
print(result)
result2 = function_with_uncommon_error(5)
print(result2)