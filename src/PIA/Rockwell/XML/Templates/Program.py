try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *

class Program():
    '''
    Program Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, Name, Type = "Normal", Description = ""):
            #Initialize Member Attributes
            assert isValidTag(Name)
            self.root = etree.Element("Program")
            self.root.set("Name", Name)
            self.root.set("Type", Type)
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

    def setMainRoutine(self, RoutineName):
        assert type(RoutineName) == str
        self.root.set("MainRoutineName", RoutineName)

    def checkIfChild(self, nodeTag):
        assert type(nodeTag) == str
        for node in self.root:
            if node.tag == NodeTag: return False
        return True

    def addRoutine(self, Routine):
        assert etree.iselement(Routine.getLocalRoot()) and Routine.getLocalRoot().tag == "Routine"
        if not self.checkIfChild("Routines"):
            self.Routines = etree.SubElement(self.root, "Routines")
        self.Routines.append(Routine)

    def addTag(self, Tag):
        assert etree.iselement(Tag.getLocalRoot()) and Tag.getLocalRoot().tag == "Tag"
        if not self.checkIfChild("Tags"):
            self.Tags = etree.SubElement(self.root, "Tags")
        self.Tags.append(Tag)

    def setAttribute(self, **kwargs):
        for key in kwargs:
            if not key in self.root.keys():
                raise KeyError("Program has No Attribute: <%s>" % key)

        for key in kwargs:
            self.root.set(key, kwargs[key])

    def setDescription(self, Description):
        assert type(Description) == str
        if self.Desc == None:
            self.Desc = etree.SubElement(self.root, 'Description')
            self.root.append(self.Desc)
        self.Desc.text = etree.CDATA(Description)

    def setParent(self, parent):
        assert etree.iselement(root) and root.tag == "Programs"
        root.append(self.root)

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)
