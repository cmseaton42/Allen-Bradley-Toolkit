from enum import Enum

class CommonType(Enum):
    '''
    abstraction interface, meant for inheritance purposes only
    '''
    BaseTypeList = []

    BOOL = "BIT"
    BaseTypeList.append(BOOL)

    SINT = "SINT"
    BaseTypeList.append(SINT)

    INT  = "INT"
    BaseTypeList.append(INT)

    DINT = "DINT"
    BaseTypeList.append(DINT)

    REAL = "REAL"
    BaseTypeList.append(REAL)

    STRING = "STRING"
    BaseTypeList.append(STRING)

    COUNTER = "COUNTER"
    BaseTypeList.append(COUNTER)

    TIMER = "TIMER"
    BaseTypeList.append(TIMER)

    def isCommonType(self, Datatype):
        return Datatype in CommonType.BaseTypeList
