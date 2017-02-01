try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *

class Tag():
    '''
    Tag Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, TagName, DataType, TagType =  "Base", Description = "", Radix = "Decimal", Constant = "false", ArrayLength = 0):
            #Initialize Member Attributes
            assert isValidTag(TagName)
            self.root = etree.Element('Tag')
            self.root.set("Name", TagName)
            self.root.set("TagType", TagType)
            self.root.set("Datatype", str(DataType))
            self.root.set("Dimension",str(ArrayLength))
            self.root.set("Radix", Radix)
            self.root.set("ExternalAccess", "Read/Wdrite")
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

    def setUsage(self, Usage):
        assert Usage == "Input" or Usage == "Output" or Usage == "InOut" or Usage == "Public"
        self.root.set("Usage", Usage)

    def setAlias(self, TagName):
        self.root.set("AliasFor", TagName)

    def setClassAttribute(self, classAttribute):
        assert classAttribute == "Standard" or classAttribute == "Safety"
        self.root.set("Class", classAttribute)

    def setAttribute(self, **kwargs):
        for key in kwargs:
            if not key in self.root.keys():
                raise KeyError("Member has No Attribute: <%s>" % key)

        for key in kwargs:
            self.root.set(key, kwargs[key])

    def setDescription(self, Description):
        assert type(Description) == str
        if self.Desc == None:
            self.Desc = etree.SubElement(self.root, 'Description')
            self.root.append(self.Desc)
        self.Desc.text = etree.CDATA(Description)

    def setParent(self, root):
        assert etree.iselement(root) and root.tag == "Tags"
        root.append(self.getLocalRoot())

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)
