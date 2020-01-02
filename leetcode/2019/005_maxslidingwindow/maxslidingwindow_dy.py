class Heap:
    def __init__(self):
        self.q = [None] # idx starts from 1
        self.parent = lambda idx: int(idx/2)
    
    def last_idx(self):
        return len(self.q)-1
    
    def exists(self, idx):
        return self.last_idx() >= idx
    
    def larger_than(self, idx, idx2):
        return self.q[idx][0] > self.q[idx2][0] or \
                (self.q[idx][0] == self.q[idx2][0] and self.q[idx][1] < self.q[idx2][1])
    
    def swap(self, idx, idx2):
        temp = self.q[idx]
        self.q[idx] = self.q[idx2]
        self.q[idx2] = temp
    
    def insert(self, node): # node is tuple of value & idx in 'nums'
        self.q.append(node)
        
        i = self.last_idx()
        while i > 1:
            parent = self.parent(i)
            if self.larger_than(i, parent):
                self.swap(i, parent)
                i = parent
            else:
                break
                
    def getMax(self):
        return self.q[1]
    
    def delete(self, idx=1):
        self.swap(idx, self.last_idx())
        self.q.pop(self.last_idx())
        self.heapify(idx)

    def heapify(self, idx):
        if idx > self.last_idx():
            return
        
        leftchild_idx = idx * 2
        rightchild_idx = idx * 2 + 1
        smallest = idx
        if self.exists(leftchild_idx) and self.larger_than(leftchild_idx, smallest):
            smallest = leftchild_idx
        if self.exists(rightchild_idx) and self.larger_than(rightchild_idx, smallest):
            smallest = rightchild_idx
        if smallest != idx:
            self.swap(idx, smallest)
            self.heapify(smallest)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = Heap()
        
        answers = []
        for i, num in enumerate(nums):
            heap.insert((num, i))
            
            if (i + 1) >= k:
                while True:
                    value, idx = heap.getMax()
                    if idx <= i-k:
                        heap.delete()
                    else:
                        answers.append(value)
                        break
                
        return answers
                
                
        
    
