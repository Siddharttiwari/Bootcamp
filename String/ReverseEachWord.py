def reverse(sentence):
    words=sentence.split(" ")
    result=""
    for word in words:
        result+=word[::-1]
        result+=" "
    return result

s=input()
print(reverse(s))