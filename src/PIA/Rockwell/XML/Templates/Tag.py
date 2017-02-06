try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *
from Base_Template import Base_Template

class Tag(Base_Template):
    '''
    Tag Template:
    See L5X Manual for Details,
    These members are to be used when defining a Tag.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, TagName, DataType, TagType =  "Base", Description = "", UseRadix = True, Radix = "Decimal", Constant = "false", ArrayLength = 0):
            #Initialize Member Attributes
            assert isValidTag(TagName)
            self.root = etree.Element('Tag')
            self.root.set("Name", TagName)
            self.root.set("TagType", TagType)
            self.root.set("Datatype", str(DataType))
            self.root.set("Dimension",str(ArrayLength))
            if UseRadix: self.root.set("Radix", Radix)
            self.root.set("ExternalAccess", "Read/Write")
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

    def setAsIO(self):
        self.root.set("IO","true")

    def addTagComment(self, TagComment):
        assert etree.iselement(TagComment.getLocalRoot()) and TagComment.getLocalRoot().tag == "Comment"
        if not self.checkIfChild("Comments"):
            self.Comments = etree.SubElement(self.root, "Comments")
        self.Comments.append(TagComment.getLocalRoot())

    def setUsage(self, Usage):
        assert Usage == "Input" or Usage == "Output" or Usage == "InOut" or Usage == "Public"
        self.root.set("Usage", Usage)

    def setAlias(self, TagName):
        self.root.set("AliasFor", TagName)

    def setClassAttribute(self, classAttribute):
        assert classAttribute == "Standard" or classAttribute == "Safety"
        self.root.set("Class", classAttribute)

    def setDescription(self, Description):
        assert type(Description) == str
        if self.Desc == None:
            self.Desc = etree.SubElement(self.root, 'Description')
            self.root.append(self.Desc)
        self.Desc.text = etree.CDATA(Description)

    def setParent(self, parent):
        assert etree.iselement(parent) and parent.tag == "Tags"
        parent.append(self.getLocalRoot())
