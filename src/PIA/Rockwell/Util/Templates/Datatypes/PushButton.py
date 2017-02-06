try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.Types import CommonType
from PIA.Rockwell.XML.Templates import *

class PB_OneButton(Datatype):
    def __init__(self):
        Datatype.__init__(self, "PB_OneButton")
        self.bitTarget = "XXXXXXXXXXHost"
        self.addMember(Member(self.bitTarget, CommonType.SINT, Hidden = True))
        self.addMember(Member("Push",         CommonType.BOOL, Target = self.bitTarget, BitNumber = 0))
        self.addMember(Member("State",        CommonType.BOOL, Target = self.bitTarget, BitNumber = 1))
        self.addMember(Member("Visibility",   CommonType.BOOL, Target = self.bitTarget, BitNumber = 2))
        self.addMember(Member("Ind",          CommonType.BOOL, Target = self.bitTarget, BitNumber = 3))
        self.addMember(Member("Interlock",    CommonType.BOOL, Target = self.bitTarget, BitNumber = 4))
        self.addMember(Member("ONS",          CommonType.BOOL, Target = self.bitTarget, BitNumber = 5))
        self.addMember(Member("Tmr",          CommonType.TIMER))

class PB_TwoButton(Datatype):
    def __init__(self):
        Datatype.__init__(self, "PB_TwoButton")
        self.addMember(Member("ButtonA", "PB_OneButton"))
        self.addMember(Member("ButtonB", "PB_OneButton"))
