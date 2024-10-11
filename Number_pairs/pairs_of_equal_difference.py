

def pairs_difference(k, arr):
    set_arr = set(arr)
    hashmap = {}
    for i in range(len(arr)):
        if arr[i]+k in set_arr:
            if (arr[i], arr[i]+k) in hashmap.keys():
                hashmap[(arr[i], arr[i]+k)] += 1
            else:
                hashmap[(arr[i], arr[i] + k)] = 1

    return sum(hashmap.values())

if __name__ == "__main__":
    difference_value = int(input())
    num_list = list(map(int, input().rstrip().split()))
    result = pairs_difference(difference_value, num_list)
    print(f"The number of pairs with equal difference: {result}")