from data_structures.queue import Queue


def multi_bracket_validation(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False  # Closing bracket without matching opening bracket
            opening_bracket = stack.pop()
            if bracket_pairs[opening_bracket] != char:
                return False  # Closing bracket doesn't match the corresponding opening bracket

    return len(stack) == 0  # Return True if all opening brackets have been matched and removed

