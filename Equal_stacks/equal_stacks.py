
def equal_stacks(h1, h2, h3):
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    n1, n2, n3 = len(h1), len(h2), len(h3)

    index1, index2, index3 = (0, 0, 0)
    while not sum_h1 == sum_h2 == sum_h3:
        if sum_h2 >= sum_h1 and sum_h2 >= sum_h3:
            sum_h2 -= h2[index2]
            index2 += 1
        elif sum_h1 >= sum_h2 and sum_h1 >= sum_h3:
            sum_h1 -= h1[index1]
            index1 += 1
        elif sum_h3 >= sum_h2 and sum_h3 >= sum_h1:
            sum_h3 -= h3[index3]
            index3 += 1
        if (index1 == n1) or (index2 == n2) or (index3 == n3):
            sum_h1 = 0
            break

    return sum_h1

if __name__ == "__main__":
    height1 = list(map(int, input().rstrip().split()))
    height2 = list(map(int, input().rstrip().split()))
    height3 = list(map(int, input().rstrip().split()))
    height = equal_stacks(height1, height2, height3)
    print(height)