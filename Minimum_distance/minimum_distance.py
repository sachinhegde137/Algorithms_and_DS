
def minimum_distances(int_list):
    min_d = None
    for i in range(len(int_list) - 1):
        for j in range(i+1, len(int_list)):
            if int_list[i] == int_list[j]:
                if min_d:
                    min_d = min(min_d, abs(i - j))
                else:
                    min_d = abs(i - j)

    return min_d


if __name__ == '__main__':
    integer_list = list(map(int, input().rstrip().split()))
    result = minimum_distances(integer_list)
    if result:
        print(f"Minimum distance: {result}")
    else:
        print("There are no two equal elements in the list")
