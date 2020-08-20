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
    return IsBST(tree[i][1], m, tree[i][0]-1) and IsBST(tree[i][2], tree[i][0], M)


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
