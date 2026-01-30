class Solution:
    # intuition
    # if opening parentheses increment balance | if balance is not zero -> include in ans
    # if closing parentheses decrement balance | if balance is not zero -> include in ans

    # intuition 2
    # stack : if stack is empty - push into stack | if stack is not empty -> include in ans
    # stack : if parentheses complete - pop from stack | if stack is not empty -> include in ans
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balance = 0

        for ch in s:
            if ch == "(":
                if balance > 0:
                    res.append(ch)
                balance += 1
            else: 
                balance -= 1
                if balance > 0:
                    res.append(ch)

        return "".join(res)