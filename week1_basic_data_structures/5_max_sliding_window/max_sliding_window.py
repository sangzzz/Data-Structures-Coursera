# python3
import random


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def fast_max_sliding_window(sequence, m):
    arr = sequence[0:m]
    if m == 0:
        return []
    M = max(arr)
    maximums = [M]
    for i in range(m, len(sequence)):
        if sequence[i] > M:
            maximums.append(sequence[i])
            M = sequence[i]
            arr = arr[1:] + [sequence[i]]
            continue
        arr = arr[1:] + [sequence[i]]
        if M not in arr:
            M = max(arr)
            maximums.append(M)
            continue
        maximums.append(M)
    return maximums


def stress_test():
    while True:
        n = random.randint(1, 1000)
        x = [random.randint(100, 10000) for i in range(0, n)]
        m = random.randint(1, n)
        if fast_max_sliding_window(x, m) == max_sliding_window_naive(x, m):
            print("Success")
        else:
            print(n, m)
            print(x)
            print(fast_max_sliding_window(x, m))
            print(max_sliding_window_naive(x, m))
            break


if __name__ == '__main__':
    # stress_test()
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    # print(*max_sliding_window_naive(input_sequence, window_size))

    print(*fast_max_sliding_window(input_sequence, window_size))
