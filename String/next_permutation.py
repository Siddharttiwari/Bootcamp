def permutation(string):
    string=list(string)
    index=-1
    for i in range(len(string)-2,-1,-1):
        if string[i]<string[i+1]:
            index=i
            break

    if index==-1:
        string.reverse()
        return  ''.join(string)
        
    for i in range(len(string)-1,index,-1):
        if string[i]>string[index]:
            string[i], string[index]=string[index],string[i]
            break

    string[index + 1:] = reversed(string[index + 1:])

    return ''.join(string)

string=input()
print(permutation(string))