# python3

from collections import namedtuple
import random

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def parent(i):
    if i == 0:
        return 0
    return (i-1)//2


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def siftup(i, heap):
    while i >= 0 and heap[parent(i)] > heap[i]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)


def siftdown(i, heap, size):
    m = i
    l = left(i)
    if l < size and heap[l] < heap[m]:
        m = l
    r = right(i)
    if r < size and heap[r] < heap[m]:
        m = r
    if m != i:
        heap[i], heap[m] = heap[m], heap[i]
        siftdown(m, heap, size)


def insert(i, heap, size):
    size = size + 1
    heap[size-1] = i
    siftup(size-1, heap)
    return size


def extract_min(heap, size):
    res = heap[0]
    heap[size-1], heap[0] = heap[0], heap[size-1]
    size = size - 1
    siftdown(0, heap, size)
    return res, size


def assign_jobs_fast(n, jobs):
    res = []
    size = n
    heap = [(0, i) for i in range(0, n)]
    for j in jobs:
        x, size = extract_min(heap, size)
        y = (x[0]+j, x[1])
        res.append(x[::-1])
        # x[0] += j
        size = insert(y, heap, size)
    return res


def stress_test():
    while True:
        n = random.randint(1, 10000)
        j = random.randint(1, 10000)
        jobs = [random.randint(1, 10000) for i in range(0, j)]
        assign_jobs1 = assign_jobs(n, jobs)
        assign_jobs2 = assign_jobs_fast(n, jobs)
        if assign_jobs1 == assign_jobs2:
            print("success")
        else:
            print(n, j, jobs, assign_jobs1, assign_jobs2)
            print("error")
            break


def main():
    # stress_test()
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    # assigned_jobs1 = assign_jobs(n_workers, jobs)
    # for job in assigned_jobs1:
    #     print(job.worker, job.started_at)
    assigned_jobs2 = assign_jobs_fast(n_workers, jobs)
    for job in assigned_jobs2:
        print(job[0], job[1])
    # if assigned_jobs1 == assigned_jobs2:
    #     print('jdkajsdja')


if __name__ == "__main__":
    main()
