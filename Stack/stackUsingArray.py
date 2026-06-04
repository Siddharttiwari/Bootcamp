class stack:
    def __init__(self):
        self.__data=[]
        self.capacity = n
        
    def isFull(self):
        return len(self.__data) == self.capacity

    def push(self,item):
        self.__data.append(item)
    
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self.__data.pop()
    def top(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self.__data[len(self.__data)-1]
    def size(self):
        return len(self.__data)
    def isempty(self):
        return self.size()==0

s = stack()

n = int(input())
elements = list(map(int, input().split()))

for x in elements:
    s.push(x)
s.pop()
print("Top element:", s.top())
print("Size:", s.size())