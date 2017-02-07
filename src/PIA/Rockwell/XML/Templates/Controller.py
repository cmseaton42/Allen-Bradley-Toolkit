try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from PIA.Rockwell.XML.Tools import *
from Base_Template import Base_Template

class Controller(Base_Template):
    '''
    Controller Template:
    See L5X Manual for Details,
    These members are to be used when defining a Controller.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, Name, Use = "Context", Description = ""):
            #Initialize Member Attributes
            assert isValidTag(Name)
            self.root = etree.Element('Controller')
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

    def addDatatype(self, Datatype):
        assert etree.iselement(Datatype.getLocalRoot()) and Datatype.getLocalRoot().tag == "Datatype"
        if not self.checkIfChild("Datatypes"):
            self.Datatypes = etree.SubElement(self.root, "Datatypes")
        self.Datatypes.append(Datatype.getLocalRoot())

    def addModule(self, Module):
        assert etree.iselement(Module.getLocalRoot()) and Module.getLocalRoot().tag == "Module"
        if not self.checkIfChild("Modules"):
            self.Modules = etree.SubElement(self.root, "Modules")
        self.Modules.append(Module.getLocalRoot())


    def addAddOnInstructionDefinition(self, AddOnInstructionDefinition):
        assert etree.iselement(AddOnInstructionDefinition.getLocalRoot()) and AddOnInstructionDefinition.getLocalRoot().tag == "AddOnInstructionDefinition"
        if not self.checkIfChild("AddOnInstructionDefinitions"):
            self.AddOnInstructionDefinitions = etree.SubElement(self.root, "AddOnInstructionDefinitions")
        self.AddOnInstructionDefinitions.append(AddOnInstructionDefinition.getLocalRoot())

    def addTag(self, Tag):
        assert etree.iselement(Tag.getLocalRoot()) and Tag.getLocalRoot().tag == "Tag"
        if not self.checkIfChild("Tags"):
            self.Tags = etree.SubElement(self.root, "Tags")
        self.Tags.append(Tag.getLocalRoot())

    def addProgram(self, Program):
        assert etree.iselement(Program.getLocalRoot()) and Program.getLocalRoot().tag == "Program"
        if not self.checkIfChild("Programs"):
            self.Programs = etree.SubElement(self.root, "Programs")
        self.Programs.append(Program.getLocalRoot())

    def addTask(self, Task):
        assert etree.iselement(Task.getLocalRoot()) and Task.getLocalRoot().tag == "Task"
        if not self.checkIfChild("Tasks"):
            self.Tasks = etree.SubElement(self.root, "Tasks")
        self.Tasks.append(Task.getLocalRoot())

    def setParent(self, parent):
        assert etree.iselement(parent) and parent.tag == "Members"
        parent.append(self.getLocalRoot())
