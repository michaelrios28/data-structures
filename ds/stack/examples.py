
def reverse(x):
    output = [None] * len(x)
    output_index = len(x) - 1
    for c in x:
        output[output_index] = c
        output_index -= 1
    return ''.join(output)

# print(reverse("Hi"))


exp = "(2+2)"


def isBalanced(input):
    brackets = {
        '(': ')',
        '[': ']',
        '<': '>',
    }
    left_brackets = [*brackets]
    right_brackets = [*brackets.values()]

    stack = []
    for c in input:
        if c in left_brackets:
            stack.append(c)

        if c in right_brackets:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if c in right_brackets and brackets[top] != c:
                return False

    return len(stack) == 0


print(isBalanced(exp))
