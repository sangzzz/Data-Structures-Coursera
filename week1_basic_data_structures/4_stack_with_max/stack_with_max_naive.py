# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)


if __name__ == '__main__':
    # stack = StackWithMax()
    stack = []
    maximumStack = []
    output = []
    num_queries = int(input())
    for _ in range(num_queries):
        query = input().split()

        if query[0] == "push":
            stack.append(int(query[1]))
            if len(maximumStack) == 0:
                maximumStack = [stack[-1]]
            if stack[-1] >= maximumStack[-1]:
                maximumStack.append(stack[-1])
        elif query[0] == "pop":
            if stack[-1] == maximumStack[-1]:
                maximumStack = maximumStack[0:-1]
            stack = stack[0:-1]
        elif query[0] == "max":
            output.append(maximumStack[-1])
        else:
            assert(0)
    for i in output:
        print(i)
