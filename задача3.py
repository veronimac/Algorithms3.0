""" Сложность алгоритма O(n). Реализован обход в ширину для определения среднего значения уровня погружения """


def averageOfLevels(self, root):
    q = [(root, 1)]
    dp = []
    max_depth = 1
    total, count = 0, 0
    while q:  # Обход в ширину
        cur_var, depth = q.pop(0)
        if depth == max_depth:  # У нас есть два варианта: мы на том же уровне погружения или уже ниже. Если на след, вносим предыдущее значение в dp, нет - увеличиваем счетчики
            count += 1
            total += cur_var.val
        elif depth > max_depth:
            max_depth = depth
            dp.append(total / count)
            total, count = cur_var.val, 1
        if cur_var.left:  #
            q.append((cur_var.left, depth + 1))

        if cur_var.right:
            q.append((cur_var.right, depth + 1))
    dp.append(total / count)  # Добавляем последнее значение отдельно, потому что условие на добавление не выполняется

    return dp