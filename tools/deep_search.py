from collections import deque


def validBraces(string):
    braces = {"[": "]", "{": "}", "(": ")"}
    stack = deque()
    for c in string:
        if c in braces:
            stack.append(c)
        elif len(stack) == 0 or braces[stack.pop()] != c:
            return False
    return len(stack) == 0


def test_braces():
    print(validBraces("(}"))
    print(validBraces("()]"))
    print("]" in {"[": "]", "{": "}", "(": ")"})


def walk(arr, step):
    n = len(arr)
    if n - step - 1 < 0:
        return
    was_any = False
    for i in range(step, n - step):
        was_any = True
        yield arr[step][i]

    for i in range(step + 1, n - step):
        was_any = True
        yield arr[i][n - step - 1]

    for i in range(n - step - 2, step, -1):
        was_any = True
        yield arr[n - step - 1][i]

    for i in range(n - step - 1, step, -1):
        was_any = True
        yield arr[i][step]
    if was_any:
        yield from walk(arr, step + 1)


def snail(arr):
    return list(walk(arr, 0))


if __name__ == '__main__':


    print(snail([[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]))
    print(snail([[1]]))
