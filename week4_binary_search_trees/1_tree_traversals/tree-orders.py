# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inord(self, i):
        if i == -1:
            return True
        self.inord(self.left[i])
        self.result.append(self.key[i])
        self.inord(self.right[i])

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.inord(0)
        return self.result

    def pre(self, i):
        if i == -1:
            return True
        self.result.append(self.key[i])
        self.pre(self.left[i])
        self.pre(self.right[i])

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.pre(0)
        return self.result

    def post(self, i):
        if i == -1:
            return True
        self.post(self.left[i])
        self.post(self.right[i])
        self.result.append(self.key[i])

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.post(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
