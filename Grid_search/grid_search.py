
def gridSearch(grid, pattern):
    pattern_found = False
    g_rows = len(grid)
    p_rows = len(pattern)
    g_cols = len(grid[0])
    p_cols = len(pattern[0])

    for i in range(g_rows-p_rows+1):
        if pattern[0] not in grid[i]:
            continue

        for k in range(g_cols-p_cols+1):
            if pattern[0] != grid[i][k:k + p_cols]:
                continue

            for j in range(1, p_rows):
                sliced_string = grid[i+j][k:(k+p_cols)]
                if sliced_string == pattern[j]:
                    if j == (p_rows-1):
                        pattern_found = True
                    else:
                        continue
                else:
                    break
    return pattern_found
    

if __name__ == '__main__':
    rows_cols = input().rstrip().split()

    grid_rows = int(rows_cols[0])
    grid_cols = int(rows_cols[1])
    grid = []

    for _ in range(grid_rows):
        grid_item = input()
        grid.append(grid_item)

    rows_cols_p = input().rstrip().split()

    pattern_rows = int(rows_cols_p[0])
    pattern_cols = int(rows_cols_p[1])
    pattern = []

    for _ in range(r):
        pattern_item = input()
        pattern.append(pattern_item)

    pattern_exists = gridSearch(grid, pattern)
    if pattern_exists:
        print("The pattern exists in the grid")
    else:
        print("The pattern DOES NOT exist in the grid")

