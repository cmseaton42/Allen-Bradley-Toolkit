try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from enum import Enum

class Member():
    def __init__(self, TagName, DataType, Hidden = False, Description = "", Radix = "Decimal", ArrayLength = 0, Target = "", BitNumber = 0):
            self.root = etree.Element('Member')
            self.root.set("Name", TagName)
            self.root.set("Datatype", DataType)
            self.root.set("Dimension",str(ArrayLength))
            self.root.set("Radix", Radix)
            if DataType = "BIT":
                self.root.set("Hidden", "false")
                self.root.set("Target", Target)
                self.root.set("BitNumber", str(BitNumber))
            elif Hidden = True:
                self.root.set("Hidden", "true")
            else:
                self.root.set("Hidden", "false")
            self.root.set("ExternalAccess", "Read/Write")
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.root.append(self.Desc)

    def setParent(self, root):
        assert etree.iselement(root) and root.tag == "Members"
        root.append(self.getLocalRoot())

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)


# class Datatype():
#     def __init__(self,):
