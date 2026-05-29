def reverse(string):
    reverseWord=""
    for i in range(len(string)-1,-1,-1):
        reverseWord+=string[i]
    return reverseWord
def palindrome(string):
    if string==reverse(string):
        print("palindrome")
    else:
        print("Not palindrome")

string=input()
palindrome(string)



