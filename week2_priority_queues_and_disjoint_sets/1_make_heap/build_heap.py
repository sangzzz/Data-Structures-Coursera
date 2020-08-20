# # python3

# import random


# def build_heap(data):
#     """Build a heap from ``data`` inplace.

#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] < data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps


# # def siftdown(i):
# #     if i

# def parent(i):
#     if i == 0:
#         return 0
#     return (i-1)//2


# def left(i):
#     return 2*i + 1


# def right(i):
#     return 2*i + 2


# # def heapify(i, size, heap):
# #     heap[size] = i
# #     x = siftup(size, heap)
# #     size += 1


# # def build_heap_fast(data, heap):
# #     # for j, i in enumerate(data):
# #     #     heapify(i, j, heap)
# #     for j in range(len(data)-1, -1, -1):
# #         heapify(data[j], j, heap)
# def siftup(i, heap, swaps):
#     # x = parent(i)
#     # if i == x:
#     #     return True
#     # if heap[x] > heap[i]:
#     #     heap[x], heap[i] = heap[i], heap[x]
#     #     req.append([x, i])
#     #     siftup(x, heap)
#     while i >= 0 and heap[parent(i)] > heap[i]:
#         heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
#         swaps.append([parent(i), i])
#         i = parent(i)


# def stress_test():
#     while True:
#         n = random.randint(1, 10)
#         data = [random.randint(1, 10) for i in range(0, n)]
#         swaps1 = build_heap(data)
#         swaps2 = []
#         for i in range(n-1, -1, -1):
#             siftup(i, data, swaps2)
#         # assert len(swaps1) == len(swaps2), "Error"
#         if swaps1 != swaps2:
#             print(data, swaps1, swaps2)
#             break
#         print("Success")


# def main():
#     # stress_test()

#     n = int(input())
#     data = list(map(int, input().split()))
#     assert len(data) == n
#     heap = [i for i in data]
#     swaps = build_heap(data)

#     # print(len(swaps))
#     # for i, j in swaps:
#     #     print(i, j)
#     # # build_heap_fast(data, heap)
#     swaps = []
#     for i in range(n-1, -1, -1):
#         siftup(i, heap, swaps)
#     print(len(swaps))
#     for x in swaps:
#         print(x[0], x[1])


# if __name__ == "__main__":
#     main()
def siftup(i):
    while i >= 0 and data[parent(i)] > data[i]:
        data[parent(i)], data[i] = data[i], data[parent(i)]
        swaps.append([parent(i), i])
        i = parent(i)


def siftdown(i):
    # print(i)
    m = i
    l = left(i)
    if l < len(data) and data[l] < data[m]:
        m = l
    r = right(i)
    if r < len(data) and data[r] < data[m]:
        m = r
    if m != i:
        data[m], data[i] = data[i], data[m]
        swaps.append([i, m])
        siftdown(m)


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    if i == 0:
        return 0
    return (i-1)//2


n = int(input())
data = list(map(int, input().split()))
swaps = []
for i in range((n-1)//2, -1, -1):
    siftdown(i)
print(len(swaps))
for i in swaps:
    print(i[0], i[1])
