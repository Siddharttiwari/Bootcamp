def vowels(string):
    s=""
    for ch in string:
        if ch not in "aeiouAeiou":
            s+=ch
    return s

string=input()
print(vowels(string))
