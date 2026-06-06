def nextGreaterElements(self, nums):
        n=len(nums)
        ans=[-1]*n
        st=[]
        for i in range(2*n-1,-1,-1):
            ind=i%n
            currele=nums[ind]
            while st and st[-1]<=currele:
                st.pop()
            if i<n:
                if st:
                    ans[i]=st[-1]
            st.append(currele)
        return ans