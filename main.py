from BNFParser import PrimitiveParse as parse
from chain import Chain,Sum
from scalar import Scalar
from generator import generator
def __getChain(defs):

    chains=dict([[name,Chain([])] for name in defs])
    def createChain(str):
        links=list(map(lambda c: chains[c] if c.isupper() else Scalar(c),str))
        return Chain(links)

    for val in defs:
        cont=[]
        for option in defs[val]:
            cont.append(createChain(option))
        else:
            if len(cont)>1:
                chains[val].append(Sum(cont))  
            else: 
                chains[val].extend(cont)
    return chains
# chains=__getChain(defs),__getChain(defs2),__getChain(defs3),__getChain(defs4),__getChain(defs5),__getChain(defs6)

def ParseAndGenerate(BNF,root="S",limit=float('inf')):
    """This is a Generator Object"""
    # try:
    tree=__getChain(parse(BNF))
    # except BaseE1xError("BNF Syntax Error")
    g=generator(tree[root])
    n=1
    try:
        for i in g:
            if n>limit:
                return
            n+=1
            yield i        
    except:
        raise BaseException("Critial Engine Error")
# for ch in ParseAndGenerate(chains[4]):
#     for each in ch:
#         print(each,end="")
#     else:
#         print()