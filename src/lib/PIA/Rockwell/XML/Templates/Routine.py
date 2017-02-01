try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from lib.PIA.Rockwell.XML.Tools import *

class Routine():
    '''
    Routine Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
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

    def checkIfChild(self, nodeTag):
        assert type(nodeTag) == str
        for node in self.root:
            if node.tag == NodeTag: return False
        return True

    def addRung(self, Rung):
        assert etree.iselement(Rung.getLocalRoot()) and Rung.getLocalRoot().tag == "Rung"
        if not self.checkIfChild("RLLContent"):
            self.RLLContent = etree.SubElement(self.root, "RLLContent")
        self.RLLContent.append(Rung)

    def setAttribute(self, **kwargs):
        for key in kwargs:
            if not key in self.root.keys():
                raise KeyError("Routine has No Attribute: <%s>" % key)

        for key in kwargs:
            self.root.set(key, kwargs[key])

    def setDescription(self, Description):
        assert type(Description) == str
        if self.Desc == None:
            self.Desc = etree.SubElement(self.root, 'Description')
            self.root.append(self.Desc)
        self.Desc.text = etree.CDATA(Description)

    def setParent(self, parent):
        assert etree.iselement(root) and root.tag == "Routines"
        root.append(self.root)

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)
