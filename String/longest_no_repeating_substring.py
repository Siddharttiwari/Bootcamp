def longest_non_repeating_substring(string):
    n = len(string)
    hash = [-1] * 256
    hashlen = len(hash)

    for i in range(hashlen):
        hash[i] = -1

    left, right, maxlen = 0, 0, 0

    while right < n:
        if hash[ord(string[right])] != -1:
            left = max(hash[ord(string[right])] + 1, left)

        currlen = right - left + 1
        maxlen = max(currlen, maxlen)

        hash[ord(string[right])] = right
        right += 1

    return maxlen


string = input()
print(longest_non_repeating_substring(string))