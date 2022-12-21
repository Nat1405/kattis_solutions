import sys
import math

class BinaryTree:
    def __init__(self):
        self.backing = [None] # 1-indexing, first element empty

    def pushBack(self, x):
        self.backing.append(x)

    @staticmethod
    def parent(i):
        return i//2

    @staticmethod
    def left(i):
        return 2*i

    @staticmethod
    def right(i):
        return 2*i+1

    def getSize(self):
        return len(self.backing)-1

    def __str__(self):
        out_str = ""
        # A new line for each level...
        for level in range(math.ceil(math.log(self.getSize(), 2))):
            # And add up all the new elements
            for i in range(2**level):
                try:
                    out_str += str(self.backing[(2**level)+i]) + ' '
                except IndexError:
                    # Incomplete binary tree
                    break
            out_str += '\n'
        
        return out_str

    def bubble_up(self, idx):
        while idx > 1:
            if self.backing[idx] > self.backing[self.parent(idx)]:
                tmp = self.backing[idx]
                
                self.backing[idx] = self.backing[self.parent(idx)]
                self.backing[self.parent(idx)] = tmp

                idx = self.parent(idx)
            else:
                break

    def push(self, x):
        self.pushBack(x)
        self.bubble_up(self.getSize())



b = BinaryTree()

b.push('a')
b.push('b')
b.push('c')
b.push('d')
b.push('e')
b.push('f')

print(b)




