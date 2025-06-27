def spiral_generator(n):
    matrix = [[0] * n for _ in range(n)]
    x, y = n // 2, n // 2
    dx, dy = 0, -1
    num = 1

    for _ in range(n * n):
        if -n // 2 < x <= n // 2 and -n // 2 < y <= n // 2:
            matrix[y][x] = num
            yield num
            num += 1

        if x == y or (x < y and x + y < n - 1) or (x > y and x + y >= n):
            dx, dy = -dy, dx

        x, y = x + dx, y + dy