def all_permutations(s, ans=""):
    if len(s) == 0:
        print(ans)
        return

    for i in range(len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:]
        all_permutations(rest, ans + ch)

all_permutations(input())