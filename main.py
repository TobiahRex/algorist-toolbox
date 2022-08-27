def check_if_sum_possible(arr, k, n=0, total=0):
    if n == len(arr):
        return True if (arr and total == k) else False
    if check_if_sum_possible(arr, k, n + 1, total):
        return True
    total += arr[n]
    if total == k:
        return True
    if check_if_sum_possible(arr, k, n + 1, total):
        return True
    if total > 0:
        total -= arr[n]
    else:
        total += arr[n]
    return False



if __name__ == '__main__':
    arr = [-10, 10]
    k = 0
    test = {
        "arr": [-2, -2, 0, -3, -3],
        # "arr": [-2, -2, 0, -3, -3, -4, 4, 3, 0, -2, -3, 2, -4, -2, 2, -2, -2, 0],
        "k": -10
    }
    print(check_if_sum_possible(**test))
{
    "arr": [0, 0, 2, 2, 1, 0, -2, 3, -1, -1, 4, 1, 2, -2, 0, -4, 1, -1],
    "k": -22
}
{
    "arr": [-2, -2, 0, -3, -3, -4, 4, 3, 0, -2, -3, 2, -4, -2, 2, -2, -2, 0],
    "k": -35
}
