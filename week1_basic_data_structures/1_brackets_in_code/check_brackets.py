# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    count = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            count.append(i+1)

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i+1
            left = opening_brackets_stack.pop()
            x = count.pop()
            if not are_matching(left, next):
                return i+1

                # print(i, opening_brackets_stack)
    if len(opening_brackets_stack) == 0:
        return 0
    else:
        return count[0]


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
