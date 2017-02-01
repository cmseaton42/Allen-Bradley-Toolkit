try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from lib.PIA.Rockwell.XML.Tools import *

class Member():
    '''
    Member Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, TagName, DataType, Hidden = False, Description = "", Radix = "Decimal", ArrayLength = 0, Target = "", BitNumber = 0):
            #Initialize Member Attributes
            assert isValidTag(TagName)
            if DataType == "BOOL": DataType = "BIT"
            self.root = etree.Element('Member')
            self.root.set("Name", TagName)
            self.root.set("Datatype", str(DataType))
            self.root.set("Dimension",str(ArrayLength))
            self.root.set("Radix", Radix)
            if DataType == "BIT":
                #Reference Rockwell Manuals for Bit Overlays for details on the following assertion.
                if Target == "": raise ValueError("Data of Type BOOL<BIT> Must have a Target: eg. target = 'ZZZZZZZZZZSample0'")
                self.root.set("Hidden", "false")
                self.root.set("Target", Target)
                self.root.set("BitNumber", str(BitNumber))
            elif Hidden == True:
                self.root.set("Hidden", "true")
            else:
                self.root.set("Hidden", "false")
            self.root.set("ExternalAccess", "Read/Write")
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

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
        assert etree.iselement(root) and root.tag == "Members"
        root.append(self.getLocalRoot())

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)
