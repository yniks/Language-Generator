from Iterators import PowerFlattenIterator as pfi
from scalar import Scalar
from chain import Sum,Chain
# class generator():
#     def getiter(self):return self._pfi
#     def __repr__(self):return "< Chain Generator >"
#     def __str__(self):return self.__repr__()
#     def __init__(self,chain):
#         self.clear()
#         self._pfi=pfi(self)
#         self._pfi_base=self._pfi.getState()
#         for link in chain.getiter():
#             if type(link)==Scalar:
#                 self.append(str(link))
#             else:
#                 self.append(generatorSum(link))
#     def __iter__(self):        return self
#     def __next__(self):
#         if self._chain_finished or len(self)==0:raise StopIteration("Stop")

#         for link in range(len(self),0,-1):
#             link=self[link]
#             try:
#                 if type(link)==generatorSum:
#                     next(link)
#                     break
#             except:pass
#         else: 
#             self._chain_finished=True
        
#         self._pfi.setState(self._pfi_base)
#         return self._pfi



# class generatorSum(generator):
#     def __repr__(self):return "< Sum Generator >"
#     __iter=None
#     __begin_state=None
#     def __init__(self,sum):
#         self._pfi=pfi(self)
#         self._pfi_base=self._pfi.getState()
#         self.__iter=sum.getiter()
#         self.__begin_state=self.__iter.getState()
#         self.__reinit__()

#     def __reinit__(self):
#         self.__iter.setState(self.__begin_state)
#         super().__init__(next(self.__iter))

#     def __next__(self):
#         try:
#             super().__next__()
#         except StopIteration as a:
#             try:
#                 super().__init__(next(self.__iter))
#                 self._chain_finished=False
#                 super().__next__()
#             except BaseException as s:
#                 self.__iter.setState(self.__begin_state)
#                 self.clear()
#                 self._pfi.setState(self._pfi_base)
#                 raise StopIteration("Stop")
#         return self._pfi

# # chain=[]
# # def generate(chain=None):


# class generator(SymetricalList):
#     def __repr__(self):return "< Chain Generator >"
#     _chains=None
#     def __init__(self,chain):
#         if type(chain)==Chain:
#             chain=Sum([chain])
#         self._chains=pfi(chain)
#     def __reinit__(self):
#         self._chains.setState()
#         self.__next_chain_()
#     def __incremnent__(self):
#         for i in range(len(self),0,-1):
#             if type(self[i])==generator:
#                 try:
#                     next(self[i])
#                     break
#                 except:pass
#         else:
#             raise StopIteration

#     def __next_chain_(self):
#         self.clear()
#         for link in next(self._chains):
#             if type(link):
#                 self.append(str(link))
#             else:
#                 self.append(generator(link))
#                 self[-1].__reinit__()

#     def __iter__(self):
#         self.__reinit__()
#         return self

#     def __next__(self):
#         try:
#             self.__incremnent__()
#         except:
#             try:
#                 self.__next_chain_()
#             except:
#                 self.__reinit__()
#                 raise StopIteration
#         return pfi(self)
from collections import UserList
class generator(list):
    chain=None
    chains=None
    baseState=None
    def __init__(self,iterable):
        self.chains=pfi(iterable if type(iterable)==Sum else Sum([iterable]))
        self.baseState=self.chains.getState()
        self=[]
    def reset(self):
        self.chains.setState(self.baseState)

    def rotate_current(self):
        for link in reversed(self):
            if type(link)==generator:
                try:
                    next(link)
                    break
                except:pass
        else:
            raise StopIteration

    def next_chain(self):
        self.clear()
        try:
            chain=pfi(next(self.chains))
            for link in chain:
                if type(link)==Scalar:
                    self.append(str(link))
                else:
                    sum=generator(link)
                    self.append(sum)
                    next(sum)
            else:pass
        except BaseException as e:
            raise StopIteration
    def __next__(self):
        try:
            self.rotate_current()
        except:
            try:
                self.next_chain()
            except:
                self.reset()
                next(self)
                raise StopIteration
        return pfi(self)
    def __iter__(self):
        return self