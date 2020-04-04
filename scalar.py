class Scalar:
    __symbol=None
    def __str__(self):return self.__symbol
    def __repr__(self):return self.__str__()
    def __init__(self,symbol):
        self.__symbol=symbol
    def __eq__(self,otherScalar):
        if type(otherScalar)!=Scalar:return False
        return self.__symbol==otherScalar.__symbol
    def __bool__(self):return bool(self.__symbol)