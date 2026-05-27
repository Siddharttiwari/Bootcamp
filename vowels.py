def vowels(s):
    count=0
    for ch in s:
        if ch in "aeiouAEIOU":
            count+=1
    return count

if __name__=="__main__":
    s=input()
    print(vowels(s))