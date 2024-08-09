"""
Daily Temperatures

You are given an array of integers temperatures where temperatures[i]
represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day
before a warmer temperature appears on a future day.
If there is no day in the future where a warmer temperature will appear
for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]

Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100

"""

# O(n^2)
def daily_temperatures_2 (temperatures):
    temps = []

    for i in range(len(temperatures) - 1):
        temp1 = temperatures[i]
        for j in range(i+1, len(temperatures)):
            temp2 = temperatures[j]
            if temp2 > temp1:
                temps.append(j - i)
                break
        if i >= len(temps):
            temps.append(0)
    temps.append(0)

    return temps


# O(n)
def daily_temperatures (temperatures):
    stack = []
    # O(n)
    res = [0 for i in temperatures]

    # O(2n) => O(n)
    for i in range(len(temperatures)):
        temp = temperatures[i]
        if len(stack) == 0:
            stack.append((temp, i))
            continue

        while len(stack) > 0 and temp > stack[-1][0]:
            res[stack[-1][1]] = i - stack[-1][1]
            stack.pop()

        stack.append((temp, i))

    return res


# temperatures = [30,38,30,36,35,40,28]
# temperatures = [22,21,20]
# op = daily_temperatures(temperatures)
# print(op)
