try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.Types import CommonType
from PIA.Rockwell.XML.Templates import *

class Alarm(Datatype):
    def __init__(self):
        Datatype.__init__(self, "ST_Alarms")
        self.addMember(Member("Word",    CommonType.DINT))
        self.addMember(Member("Compare", CommonType.DINT))
        self.addMember(Member("ONS",     CommonType.DINT))
        self.addMember(Member("TMR",     CommonType.TIMER))
        self.addMember(Member("CNT",     CommonType.COUNTER))
