#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def IsBST(i, m, M):
    if i == -1:
        return True
    elif tree[i][0] < m or tree[i][0] > M:
        return False
    return IsBST(tree[i][1], m, tree[i][0]-1) and IsBST(tree[i][2], tree+1, M)

# def inorder(i, tree, traversal):
#     if tree[i][1] != -1:
#         inorder(tree[i][1], tree, traversal)
#     traversal.append(tree[i][0])
#     if tree[i][2] != -1:
#         inorder(tree[i][2], tree, traversal)


# def IsBinarySearchTree(tree):
#     # Implement correct algorithm here
#     inorder_traversal = []
#     inorder(0, tree, inorder_traversal)
#     for i in range(len(inorder_traversal)-1):
#         if inorder_traversal[i] > inorder_traversal[i+1]:
#             return False
#     return True


def main():
    nodes = int(input().strip())
    global tree, int_min, int_max
    tree, int_min, int_max = [], -(2**31), 2**31 - 1
    for i in range(nodes):
        tree.append(list(map(int, input().strip().split())))

    if nodes <= 1:
        print("CORRECT")
        sys.exit(0)
    if IsBST(0, int_min, int_max):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
