#| Given a string of round, curly, and square open and closing brackets,
#| return whether the brackets are balanced (well-formed).
#| For example, given the string "([])[]({})", you should return true.
#| Given the string "([)]" or "((()", you should return false.

#-----------------#
# Define Function #
#-----------------#

def is_balanced(brackets):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for bracket in brackets:
        if bracket in matching_brackets.values():
            stack.append(bracket)
        elif bracket in matching_brackets:
            if not stack or stack[-1] != matching_brackets[bracket]:
                return False
            stack.pop()
        else:
            # Invalid character
            return False

    return len(stack) == 0