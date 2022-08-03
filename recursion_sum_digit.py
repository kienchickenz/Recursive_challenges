def sum_digit(n):

    if n < 0:

        return "Error."

    if n == 0:

        return 0

    last_digit = n % 10

    return sum_digit(n // 10) + last_digit