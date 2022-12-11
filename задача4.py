""" Сложность O(n**3). За основу был взят алгоритм нахождения площади острова, но вместо площади просто добавляем в
счетчик 1."""


def numIslands(self, grid):
    seen = set()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1' and (i, j) not in seen:
                stack = [(i, j)]
                seen.add((i, j))
                while stack:
                    row, col = stack.pop()
                    for new_row, new_col in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1):
                        if 0 <= new_col < len(grid[0]) and 0 <= new_row < len(grid) and (
                                (new_row, new_col) not in seen) and grid[new_row][new_col] == "1":
                            stack.append((new_row, new_col))
                            seen.add((new_row, new_col))
                count += 1  # Остров полностью пройден, добавляем 1

    return count