def consonant(s):
    count=0
    for ch in s :
        if s not in "aeiouAEIOu":
            count+=1
    return count

if __name__=="__main__":
    s=input()
    print(consonant(s))
    
