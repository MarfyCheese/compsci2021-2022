import random 
import time 

class PyList:
    def __init__(self,contents=[], size=10):
        # The contents allows the programmer to construct a list with
        # the initial contents of this value. The initial_size
        # lets the programmer pick a size for the internal size of the 
        # list. This is useful if the programmer knows he/she is going 
        # to add a specific number of items right away to the list.
        self.items = [None] * size
        self.numItems = 0
        self.size = size
        self.appendCounter = 0

        for e in contents:
            self.append(e)
          
    def __getitem__(self,index):
        if index < self.numItems:
            return self.items[index]
        
        raise IndexError("PyList index out of range")
    
    def __setitem__(self,index,val):
        if index < self.numItems:
        	self.items[index] = val
        return
         
        raise IndexError("PyList assignment index out of range")
    
    def insert(self,i,e):
        
        if self.numItems == self.size:
            self.__makeroom()
           
        if i < self.numItems:
            for h in range(self.numItems-1,i-1,-1):
              self.items[h + 1]  = self.items[h]
            self.items[i] = e
            self.numItems += 1
            return

        else:
            self.append(e)
            return
            
            
    def __add__(self,other):
        
        result = PyList()
        
        for i in range(self.numItems):
            result.append(self.items[i])
            
        for i in range(other.numItems):
            result.append(other.items[i])
            
        return result
    
    
    def __contains__(self,item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True

        return False
    
    def __delitem__(self,index):
        for i in range(index, self.numItems-1):
            self.items[i] = self.items[i+1]
        self.numItems -= 1 # same as writing self.numItems = self.numItems - 1
            
    def __eq__(self,other):

        if type(other) != type(self):
            return False
        
        if self.numItems != other.numItems:
            return False
        
        for i in range(self.numItems):
            if self.items[i] != other.items[i]:
                return False
            
        return True
    
    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]  
            
    def __len__(self):
        return self.numItems
    
    # This method is hidden since it starts with two underscores. 
    # It is only available to the class to use. 
    def __makeroom(self):
        # increase list size by 1/4 to make more room.
        newlen = (self.size // 4) + self.size + 1
        newlst = [None] * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]
            
        self.items = newlst
        self.size = newlen        

    def append(self,item):
        if self.numItems == self.size:
            self.__makeroom()
        self.items[self.numItems] = item
        self.numItems += 1
        self.appendCounter += 1

    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "]"
        return s
    
    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "])"
        return s        
            
    def sort(self):
        pass
	
    def appendAmount(self):
        return self.appendCounter

    def resetAppend(self):
        self.appendCounter = 0
    
    def swap(self,i,j):
        if i >= self.numItems or j >= self.numItems:
            raise IndexError
        elif i == j:
            return
        else:
            j2 = self.items[j]
            self.items[j] = self.items[i]
            self.items[i] = j2
            return
    
    def isSorted(self):
        for i in range(0,self.numItems-1,2): 
            if self.items[i] > self.items[i+1]:
                return False
        return True
    
    def bubbleSort(self):
        while not self.isSorted():
            for i in range(0,self.numItems-1):
                if self.items[i] > self.items[i + 1]:
                    self.swap(i,i+1)

    def maxIndex(self,length):
        bigIndex = 0
        for i in range(length):
            if self.items[i] > self.items[bigIndex]:
                bigIndex = i
        return bigIndex
    
    def minIndex(self, length):
        smallIndex = 0
        for i in range(length):
            if self.items[i] < self.items[smallIndex]:
                smallIndex = i
        return smallIndex
    
    def insertionSort(self):
        for i in range(self.numItems - 1,1,-1):
            index = self.maxIndex(i)
            if not self.items[index] <= self.items[i]:
                self.swap(index,i)
            
            



def makeAlmostSortedPylist(length,amountSwapped):
    almostSorted = PyList()
    for i in range(length):
        almostSorted.append(i)
    if amountSwapped > 0:
        for i in range(amountSwapped):
         almostSorted.swap(random.randint(0,length-1),random.randint(0,length-1))
    return almostSorted

def makeRandomPylist(length):
    randList = list(range(length))
    random.shuffle(randList)
    return PyList(randList)

def makeBackwardPyList(length):
    backward = PyList()
    for i in range(length,0,-1):
        backward.append(i)
    return backward



def main():
    lst = PyList()
    
    for i in range(100):
        lst.append(i)
    
    lst2 = PyList(lst)
    
    print(lst)
    print(lst2)
    
    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
    
    lst3 = lst + lst2
    
    if len(lst3) == len(lst) + len(lst2):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
        
    
    if 1 in lst3:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")        
    
    if 2 in lst3:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")        
    
    del lst[1]
    
    if 1 in lst:
        print("Test 5 Failed")
    else:
        print("Test 5 Passed")        
    
    if len(lst) == 99:
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")        
        
    if lst == lst2:
        print("Test 7 Failed")
    else:
        print("Test 7 Passed")        
    
    del lst2[2]
    
    if lst == lst2:
        print("Test 8 Failed")
    else:
        print("Test 8 Passed")  
        
    
    lst4 = PyList(lst)
    lst.insert(0,100)
    lst4 = PyList([100]) + lst4
    
    if lst == lst4:
        print("Test 9 Passed")
    else:
        print("Test 9 Failed")
        
    lst.insert(1000,333)
    lst4.append(333)

    if lst == lst4:
        print("Test 10 Passed")
    else:
        print("Test 10 Failed")  
        
    print(lst)
    print(lst4)
    
    lst.swap(1,99)

    if lst[1] == 99 and lst[99] == 0:
        print("Test 11 Passed")
    else:
        print("Test 11 Failed")

    lst.append(1)
    lst.swap(100,101)
    lst.swap(0,1)
    lst.swap(0,99)
    lst.swap(1,100)
    

    if lst.isSorted():
        print("Test 12 Passed")
    else:
        print("Test 12 Failed")

    lst4.bubbleSort()
    if lst4.isSorted():
        print("Test 13 Passed")
    else:
        print("Test 13 Failed")
    # for i in range(1,1001):
        # list12 = makeBackwardPyList(i)
        # start = time.thread_time()
        # list12.bubble_sort()
        # stop = time.thread_time() - start
        # with open("backwardbubbletimes.csv","a") as f:	
            # f.write('{},{}\n'.format(i,stop))
        # print(stop)
    lst5 = makeBackwardPyList(20)

    if lst4.maxIndex(len(lst4)) == 100:
        print("Test 14 Passed")
    else:
        print("Test 14 Failed")
    
    if lst5.maxIndex(len(lst5)) == 0:
        print("Test 14.1 Passed")
    else:
        print("Test 14.1 Failed")

if __name__ == "__main__":
    main()