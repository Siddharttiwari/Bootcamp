def minInsertions(self, s: str) -> int:
        stack = []
        count = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    count += 1
                    i += 1

                if stack:
                    stack.pop()
                else:
                    count += 1

        count += 2 * len(stack)

        return count