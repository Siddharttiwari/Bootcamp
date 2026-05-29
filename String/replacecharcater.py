s=input()
pattern=input()
pat=s.find(pattern)

if pattern in s:
    s=s.replace(pattern,"#")
    print(s)
else:
    print("Pattern not found")


