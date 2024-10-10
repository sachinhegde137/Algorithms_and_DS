
def missing_numbers(arr, brr):
    f_dict_a = {}
    f_dict_b = {}
    set_arr = set(arr)
    set_brr = set(brr)

    for num in set_arr:
        f_dict_a[num] = arr.count(num)  # {2: 2, 3: 1, 4: 1, 5: 1, 8: 1}

    for num in set_brr:
        f_dict_b[num] = brr.count(num)  # {1: 1, 2: 2, 3: 1, 4:2, 5: 1, 7: 1, 8: 1, 9: 2}

    missing_num_list = []
    for num in f_dict_b.keys():
        if num not in f_dict_a.keys():
            missing_num_list.append(num)
            continue
        if f_dict_a[num] != f_dict_b[num]:
            missing_num_list.append(num)

    return missing_num_list


if __name__ == '__main__':
    arr1 = list(map(int, input().rstrip().split()))
    arr2 = list(map(int, input().rstrip().split()))

    result = missing_numbers(arr1, arr2)
    print(result)