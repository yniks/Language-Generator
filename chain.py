from Iterators import PowerFlattenIterator as pfi
from scalar import Scalar
SUCCESS=3
RIGHT_REMAINING=2
LEFT_REMAINING=1
FAILURE=0
LEN_MAX=1000

class Chain(list):

    
    def __repr__(self):
        return "Chain : "+super().__repr__()
    def getiter(self):return pfi(self,Chain)
    def __init__(self,links=[]):
        for each in links:
            if not (type(each)==Chain or type(each)==Scalar or type(each)==Sum):raise BaseException("Every item of Chain must be either Chain,Sum or scalar")
        else: self.extend(links)

    def superPose(chl,chr):
        '''
            SuperPose Operation: Returns
            Enumerate Success via follwing values:
                x : not matched
                s : exact superPose successfull
                l : left side of the chain is remaing otherwise Successfull
                r : right side of the chain is remaing otherwise successfull
        '''
        from itertools import zip_longest
        for lnode,rnode in zip_longest(chl,chr):
            if lnode==rnode:
                continue
            elif type(rnode)==Sum:
                chl._silent_prev()
                flag=rnode.rightsuperPose(chl)
                if flag<=LEFT_REMAINING:return flag
            elif type(lnode)==Sum:
                chr._silent_prev()
                flag=lnode.leftsuperPose(chr)
                if flag<=LEFT_REMAINING:return flag
            elif not lnode:
                chr._silent_prev()
                return RIGHT_REMAINING#True#raise BaseException("Lnode Emptied")
            elif not rnode:
                chl._silent_prev()
                return LEFT_REMAINING#False #raise BaseException("Rnode Emptied")
            else:
                chr._silent_prev()
                return FAILURE#False
        else:
            return SUCCESS
    #Seemmingly,Idea of Length on a chain does not make sense
    # def __len__(self):
    #     iter=self.getiter()
    #     length=0
    #     for link in iter:
    #         if length>LEN_MAX:return length
    #         elif type(link)==Scalar:length+=1
    #         elif type(link)==Sum:length+=len(link)
    #     else:
    #         return length
    def generate(self):
        pass
    @staticmethod
    def generate(ch_iter,*prev):
        string=[""]
        for link in ch_iter:
            if type(link)==Scalar:string[0]+=str(link)
            elif type(link)==Sum:
                ch_iter._silent_prev()
                return Sum.generate(ch_iter,*prev,string)
        else:
            print(*[s[0] for s in prev],string[0],sep="")

class Sum(list):

    def getiter(self):return pfi(self,Sum)
    def __repr__(self):
        return "Sum : "+super().__repr__()
    def __init__(self,chains):
        for     each in chains:
            # 
            if not type(each)==Chain:raise BaseException("Every item of Sum must be Chain")
        else:
            self.extend(chains)

    def leftsuperPose(self,chr):
        """
            wait until SUCCESS or RIGHT_REMAIN CONDITION ARRIVE then return the Same
            otherwise return the BEST state acchived in order FAILURE,left remaining,right
        """
        startState=chr.getState()
        bestYetFlag=FAILURE
        for chain in self.getiter():
            chain=chain.getiter()
            sucFlag=Chain.superPose(chain,chr)
            if sucFlag>bestYetFlag:bestYetFlag=sucFlag
            if sucFlag>=RIGHT_REMAINING:return sucFlag
            chr.setState(startState)
        else:
            return bestYetFlag

    def rightsuperPose(self,chl):
        startState=chl.getState()
        worstYetFlag=SUCCESS
        for chain in self.getiter():
            chl.setState(startState)
            chain=chain.getiter()
            sucFlag=Chain.superPose(chl,chain)
            if sucFlag<worstYetFlag:worstYetFlag=sucFlag
            if sucFlag<=LEFT_REMAINING:return sucFlag
        else:
            return worstYetFlag
    #Seemmingly,Idea of Length on a chain does not make sense
    # def __len__(self):
    #     iter=self.getiter()
    #     maxlen=0
    #     for chain in iter:
    #         lchain=len(chain)
    #         if lchain > maxlen:maxlen=lchain
    #     else:
    #         return maxlen
    # def _sort__(self):
    #     pass
    @staticmethod
    def generate(ch_iter,*prev):
        iter=next(ch_iter).getiter()
        startState=ch_iter.getState()
        for chain in iter:
            chain.generate(*prev)
def match(sl,sr):
    sri=sr.getiter()
    sli=sl.getiter()
    sucFlag=Chain.superPose(sli,sri)
    return sucFlag
    # if sucFlag==SUCCESS or sucFlag==RIGHT_REMAINING:return sucFlag
    # if Chain.superPose(sli,sri):
    #     try:
    #         next(sri)
    #         return False
    #     except:return True
    # else:return False