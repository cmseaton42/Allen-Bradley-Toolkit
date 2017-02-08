try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *
from Base_Template import Base_Template

class Program(Base_Template):
    '''
    Program Template:
    See L5X Manual for Details,
    These members are to be used when defining a program.
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

    def addRoutine(self, Routine):
        assert etree.iselement(Routine.getLocalRoot()) and Routine.getLocalRoot().tag == "Routine"
        if not self.checkIfChild("Routines"):
            self.Routines = etree.SubElement(self.root, "Routines")
        self.Routines.append(Routine.getLocalRoot())

    def addTag(self, Tag):
        assert etree.iselement(Tag.getLocalRoot()) and Tag.getLocalRoot().tag == "Tag"
        if not self.checkIfChild("Tags"):
            self.Tags = etree.SubElement(self.root, "Tags")
        self.Tags.append(Tag.getLocalRoot())

    def setParent(self, parent):
        assert etree.iselement(parent) and parent.tag == "Programs"
        parent.append(self.root)
