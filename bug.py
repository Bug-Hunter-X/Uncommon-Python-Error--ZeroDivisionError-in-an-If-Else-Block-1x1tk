def function_with_uncommon_error(x):
    if x == 0:
        return 1 / x  # ZeroDivisionError
    else:
        return x + 1

result = function_with_uncommon_error(0)
print(result)