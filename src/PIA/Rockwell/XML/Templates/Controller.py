try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *

class Controller():
    '''
    Controller Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, Name, Use = "Context", Description = ""):
            #Initialize Member Attributes
            assert isValidTag(TagName)
            self.root = etree.Element('Controller')
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

    def checkIfChild(self, nodeTag):
        assert type(nodeTag) == str
        for node in self.root:
            if node.tag == NodeTag: return False
        return True

    def addDatatype(self, Datatype):
        assert etree.iselement(Datatype.getLocalRoot()) and Datatype.getLocalRoot().tag == "Datatype"
        if not self.checkIfChild("Datatypes"):
            self.Datatypes = etree.SubElement(self.root, "Datatypes")
        self.Datatypes.append(Datatype)

    def addModule(self, Module):
        assert etree.iselement(Module.getLocalRoot()) and Module.getLocalRoot().tag == "Module"
        if not self.checkIfChild("Modules"):
            self.Modules = etree.SubElement(self.root, "Modules")
        self.Modules.append(Datatype)

    def addAddOnInstructionDefinition(self, AddOnInstructionDefinition):
        assert etree.iselement(AddOnInstructionDefinition.getLocalRoot()) and AddOnInstructionDefinition.getLocalRoot().tag == "AddOnInstructionDefinition"
        if not self.checkIfChild("AddOnInstructionDefinitions"):
            self.AddOnInstructionDefinitions = etree.SubElement(self.root, "AddOnInstructionDefinitions")
        self.AddOnInstructionDefinitions.append(Datatype)

    def addProgram(self, Program):
        assert etree.iselement(Program.getLocalRoot()) and Program.getLocalRoot().tag == "Program"
        if not self.checkIfChild("Programs"):
            self.Programs = etree.SubElement(self.root, "Programs")
        self.Programs.append(Datatype)

    def addTask(self, Task):
        assert etree.iselement(Task.getLocalRoot()) and Task.getLocalRoot().tag == "Task"
        if not self.checkIfChild("Tasks"):
            self.Tasks = etree.SubElement(self.root, "Tasks")
        self.Tasks.append(Datatype)

    def setAttribute(self, **kwargs):
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
