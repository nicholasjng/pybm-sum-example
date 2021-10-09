
def my_sum(n: int):
    result = 0
    for i in range(n):
        for _ in range(i):
            result += 1

    return result
