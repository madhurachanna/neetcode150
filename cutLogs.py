def dfs(n):
    if n == 1 or n == 3 or n == 4:
        return 1
    if n < 1:
        return float("inf")

    count = min(dfs(n - 1), dfs(n - 3), dfs(n - 4))

    return count + 1


# count = dfs(2)
# print("count = ", count)


def dfs2(p, t):
    if t == 0:
        return 0
    if t < 0:
        return float("-inf")

    count = 0
    for i in range(t):
        index = i + 1 - t
        x = dfs2(p, index)
        count = max(count, p[i] + p[index])
        print(i, index, x, count, p[i], [index])

    return count


count = dfs2([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 4)
print("count = ", count)
