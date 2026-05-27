def palindrome(nums):
    n=len(nums)
    left_ptr,right_ptr=0,n-1
    while left_ptr<right_ptr:
        if nums[left_ptr]!=nums[right_ptr]:
            return False
        left_ptr+=1
        right_ptr-=1
    return True

if __name__=="__main__":
    nums=input()
    if palindrome(nums):
        print("palindrome")
    else:
        print("Not Palindrome")

