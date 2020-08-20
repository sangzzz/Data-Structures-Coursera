# python3

import sys
import threading


class node:
    def __init__(self, val=None, val2=[]):
        self.data = val
        self.p = val2
        # self.m = 0


class linkedlist:
    def __init__(self):
        self.head = None


def height(k):
    if len(k.p) == 0:
        return 0
    h = 0
    for i in k.p:
        h = max(h, height(i))
    return 1+h


def make_tree(n, parents):
    l = linkedlist()
    nodes = []
    for i in range(0, len(parents)):
        nodes.append(node(i, []))
    for i, j in enumerate(parents):
        if j == -1:
            l.head = nodes[i]
            continue
        nodes[j].p.append(nodes[i])
    return height(l.head)


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(make_tree(n, parents))


# # # In Python, the default limit on recursion depth is rather low,
# # # so raise it here for this problem. Note that to take advantage
# # # of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# # import sys
# # import threading
# # sys.setrecursionlimit(10**7)  # max depth of recursion
# # threading.stack_size(2**27)  # new thread will get stack of such size


# # class TreeHeight:
# #     def read(self):
# #         self.n = int(input())
# #         self.parent = list(map(int, input().split()))

# #     def compute_height(self):
# #         maxHeight = 0
# #         heights = [0] * len(self.parent)
# #         for vertex in range(self.n):
# #             if (heights[vertex] != 0):
# #                 continue
# #             height = 0
# #             i = vertex
# #             while i != -1:
# #                 if (heights[i] != 0):
# #                     height += heights[i]
# #                     break
# #                 height += 1
# #                 i = self.parent[i]
# #             maxHeight = max(maxHeight, height)
# #             i = vertex
# #             while i != -1:
# #                 if (heights[i] != 0):
# #                     break
# #                 heights[i] = height
# #                 height -= 1
# #                 i = self.parent[i]
# #         return maxHeight

# #     def old_compute_height(self):
# #         maxHeight = 0
# #         for vertex in range(self.n):
# #             height = 0
# #             i = vertex
# #             while i != -1:
# #                 height += 1
# #                 i = self.parent[i]
# #             maxHeight = max(maxHeight, height)
# #         return maxHeight


# # def main():
# #     tree = TreeHeight()
# #     tree.read()
# #     print(tree.compute_height())


# # threading.Thread(target=main).start()
# import sys
# import threading
# from collections import deque, defaultdict
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)  # new thread will get stack of such size


# class TreeHeight:
#     def read(self):
#         self.n = int(sys.stdin.readline())
#         self.parent = list(map(int, sys.stdin.readline().split()))

#     def compute_height(self):
#         nodes = defaultdict(set)
#         for i in range(self.n):
#             if self.parent[i] == -1:
#                 root = i
#             else:
#                 nodes[self.parent[i]].add(i)
#         if nodes == None:
#             return
#         q, level, target, active = deque([root]), 0, root, 0
#         while q:
#             node = q.popleft()
#             if node == target:
#                 level, active = level + 1, 1
#             if nodes[node] != []:
#                 for i, child in enumerate(nodes[node]):
#                     q.append(child)
#                 if active == 1 and q:
#                     target, active = q[-1], 0
#         return level


# def main():
#     tree = TreeHeight()
#     tree.read()
#     print(tree.compute_height())


# threading.Thread(target=main).start()
