"""
Pow (x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
"""

# Devide and conquer
def my_pow(x: float, n: int) -> float:
    if n == 0 or x == 0:
        return 1

    m = abs(n) // 2

    pow = my_pow(x, m)
    pow *= pow

    # Handle extra
    if abs(n) % 2 == 1:
        pow *= x

    if n < 0:
        return 1/ pow
    return pow

# Direct
# Exceeds time limit for large values of n
def my_pow_2(x: float, n: int) -> float:
    pow = 1
    for i in range(abs(n)):
        pow *= x
    if n < 0:
        return 1/ pow
    return pow


# op = my_pow(2.00, 10)
# op = my_pow(2.1, 3)
# op = my_pow(2.0, -2)
op = my_pow(0.00001, 2147483647)
print(op)
