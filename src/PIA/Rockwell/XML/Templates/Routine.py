try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *
from Base_Template import Base_Template

class Routine(Base_Template):
    '''
    Routine Template:
    See L5X Manual for Details,
    These members are to be used when defining a ladder routine.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, Name, Description = ""):
            #Initialize Member Attributes
            assert isValidTag(Name)
            self.root = etree.Element("Routine")
            self.root.set("Name", Name)
            self.root.set("Type", "RLL")
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

    def addRung(self, Rung):
        assert etree.iselement(Rung.getLocalRoot()) and Rung.getLocalRoot().tag == "Rung"
        if not self.checkIfChild("RLLContent"):
            self.RLLContent = etree.SubElement(self.root, "RLLContent")
        self.RLLContent.append(Rung.getLocalRoot())

    def setParent(self, parent):
        assert etree.iselement(parent) and parent.tag == "Routines"
        parent.append(self.root)
