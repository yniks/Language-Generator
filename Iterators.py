class PowerFlattenIterator:

    '''Flatten Iterator,
        It Itterates over leaves of a tree
         Supports 
            -Reverse Iteration,
            -State Management of Iteration
             e.g Saving,Copying,Resuming Iteration State
    '''
    reverse=False
    _stack=[]
    def __repr__(self):return "< Faltten Tree Generator >"
    def __str__(self):return "< Flatten Tree Generator >"
    #StateManagement
    def __copy__(self):
        return self.__class__(self)
    def getState(self):return [[*x] for x in self._stack] 
    def setState(self,stack=None):self._stack=[[*x] for x in stack]  if stack else [[len(self._list) ,self._list]] if self.reverse else [[-1,self._list]]
        
    #Initialization
    def __init__(self,iterable,cls=None,stack=None):
        if isinstance(iterable,PowerFlattenIterator):
            #Copy costruction
            return self.__class__.__init__(self,iterable._list,iterable.cls,iterable._stack)
        self.cls=cls or type(iterable)
        self._list=iterable
        self.setState(stack)
        if not hasattr(iterable, '__getitem__'):raise BaseException("Base Object needs to have a __getItem__ method defined.")
        if not isinstance(iterable,self.cls):raise BaseException("Base Object should be the instance of Unwrappable class") 
    #Iterator Stuff
    def __bool__(self):
        try:
            self.current()
            return True
        except:
            return False
    def __iter__(self):
        return self
    def __reversed__(self):
        return rev_PowerFlattenIterator(self)
    def current(self):
        try:
            return self._stack[-1][1][self._stack[-1][0]]
        except:
            raise StopIteration
    def __next__(self):
        while self._stack:
            self._stack[-1][0]+=1
            index,chain=self._stack[-1]
            if index<len(chain):
                if type(chain[index])!=self.cls:
                    return chain[index]
                else:
                    self._stack.append([-1,chain[index]])
            else:
                self._stack.pop()
        else:
            self._stack.append([index,chain])
            raise StopIteration

    def __prev__(self):
        while self._stack:
            self._stack[-1][0]-=1
            index,chain=self._stack[-1]
            if index>=0:
                if type(chain[index])!=self.cls:
                    return chain[index]
                else:
                    self._stack.append([len(chain[index]),chain[index]])
            else:
                self._stack.pop()
        else:
            self._stack.append([index,chain])
            raise StopIteration
class rev_PowerFlattenIterator(PowerFlattenIterator):
    reverse=True
    def __init__(self,iterable,cls=None,stack=None):
        if isinstance(iterable,PowerFlattenIterator):
            super().__init__(iterable)
        else:
            super().__init__(iterable,cls,stack)
    def __reversed__(self):
        return PowerFlattenIterator(self)
    def __next__(self):
        while self._stack:
            self._stack[-1][0]-=1
            index,chain=self._stack[-1]
            if index>=0:
                if type(chain[index])!=self.cls:
                    return chain[index]
                else:
                    self._stack.append([len(chain[index]),chain[index]])
            else:
                self._stack.pop()
        else:
            self._stack.append([index,chain])
            raise StopIteration
    def __prev__(self):
        while self._stack:
            self._stack[-1][0]+=1
            index,chain=self._stack[-1]
            if index<len(chain):
                if type(chain[index])!=self.cls:
                    return chain[index]
                else:
                    self._stack.append([-1,chain[index]])
            else:
                self._stack.pop()
        else:
            self._stack.append([index,chain])
            raise StopIteration

# ##DEMO
# p=PowerFlattenIterator([1,[7,[3,4,5],8,[8,9,0,6]]],list)
# print(*p)
# r=reversed(p)
# for i in range(0,8):print(next(r),end=" ")
# r=reversed(r)
# print(*r)

# # print(p.__prev__())
# # print(p.__prev__())
# # print(p.__next__())
# # print(p.__prev__())
# # print(p.__next__())
# # print(p.__prev__())
# # print(p.__next__())
# # print(p.__prev__())
# # print(p.__next__())
# # print(p.__prev__())
# # print(p.__next__())
# # print(p.__prev__())
# # for x in range(10000):print(p.current(),end=" ")