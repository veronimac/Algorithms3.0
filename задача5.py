""" Считаем периметр по предыдущей задаче. Сложность O(n**3).
Вместо добавления в стек, прибавляем значение периметра. Для этого было разделено одно большое условие на несколько."""


def islandPerimeter(self, grid):
    seen = set()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and (i, j) not in seen:
                stack = [(i, j)]
                seen.add((i, j))
                while stack:
                    row, col = stack.pop()
                    for new_row, new_col in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                        if (new_row, new_col) not in seen:
                            if 0 <= new_col < len(grid[0]) and 0 <= new_row < len(grid):
                                if grid[new_row][new_col] == 1:
                                    stack.append((new_row, new_col))
                                    seen.add((new_row, new_col))
                                else:
                                    count += 1
                            else:
                                count += 1
    return count