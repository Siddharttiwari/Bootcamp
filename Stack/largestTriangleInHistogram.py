def largestRectangleArea(heights):
        n = len(heights)
        stack = []
        leftsmall = [0] * n
        rightsmall = [0] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            leftsmall[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            rightsmall[i] = n - 1 if not stack else stack[-1] - 1
            stack.append(i)
        max_area = 0
        for i in range(n):
            width = rightsmall[i] - leftsmall[i] + 1
            max_area = max(max_area, heights[i] * width)

        return max_area
        