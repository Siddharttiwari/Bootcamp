def removeduplicate(string):
    removed=""
    for char in string:
        if char not in removed:
            removed+=char
    return removed

string=input()
print(removeduplicate(string))