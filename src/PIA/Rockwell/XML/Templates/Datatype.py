try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *
from Base_Template import Base_Template

class Datatype(Base_Template):
    '''
    UDT Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, TypeName, Description = ""):
            #Initialize Member Attributes
            assert isValidTag(TypeName)
            self.root = etree.Element("Datatype")
            self.root.set("Name", TypeName)
            self.root.set("Family", "NoFamily")
            self.root.set("Class", "User")
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

            self.Members = etree.SubElement(self.root, "Members")

    def getMembersRoot(self):
        return self.Members

    def addMember(self, member):
        self.Members.append(member.getLocalRoot())

    def setParent(self, parent):
        assert etree.iselement(parent) and parent.tag == "DatatTypes"
        parent.append(self.root)
