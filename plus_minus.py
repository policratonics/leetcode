def plusMinus(arr):
    n = len(arr)
    plus = minus = zero = 0
    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
        else:
            zero += 1
    print(f"{round(plus/n, 6)}\n{round(minus/n, 6)}\n{round(zero/n, 6)}")


def miniMaxSum(arr):
    smin = 0
    for i in sorted(arr)[:-1]:
        smin += i

    smax = 0
    for i in sorted(arr)[1:]:
        smax += i

    print(sum(sorted(arr)[:-1]), sum(sorted(arr)[1:]))


if __name__ == '__main__':
    plusMinus([-4, 3, -9, 0, 4, 1])

    miniMaxSum([7, 69, 2, 221,   8974])
