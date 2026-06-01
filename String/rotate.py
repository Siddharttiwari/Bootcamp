def left_rotate(s, k):
    k = k % len(s)
    return s[k:] + s[:k]
print(left_rotate("abcd", 1))   
print(left_rotate("abcd", 2))