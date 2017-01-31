try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

from Tools import *

class Project():
    '''
    Project Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, SchemaRevision = "1.0", SoftwareRevision = "30.00"):
            #Initialize Member Attributes
            self.root = etree.Element("RSLogix5000Content")

    def getControllerRoot(self):
        return self.Controller

    def checkIfChild(self, nodeTag):
        assert type(nodeTag) == str
        for node in self.root:
            if node.tag == NodeTag: return False
        return True

    def addController(self, Controller):
        assert etree.iselement(Controller.getLocalRoot()) and Controller.getLocalRoot().tag == "Controller"
        if not self.checkIfChild("Controller"):
            self.Controller = etree.SubElement(self.root, "Controller")
        self.Controller.append(Datatype)

    def setAttribute(self, **kwargs):
        for key in kwargs:
            self.root.set(key, kwargs[key])

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)

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

class Datatype():
    '''
    UDT Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, TypeName, Description = ""):
            #Initialize Member Attributes
            assert isValidTag(TypeName)
            self.root = etree.Element("Datatype")
            self.root.set("Name", TypeName)
            self.root.set("Family", "NoFamily")
            self.root.set("Class", "User")
            if Description != "":
                self.Desc = etree.SubElement(self.root, 'Description')
                self.setDescription(Description)
                self.root.append(self.Desc)

            self.Members = etree.SubElement(self.root, "Members")

    def getMembersRoot(self):
        return self.Members

    def addMember(self, member):
        self.Members.append(member.getLocalRoot())

    def setAttribute(self, **kwargs):
        for key in kwargs:
            if not key in self.root.keys():
                raise KeyError("Datatype has No Attribute: <%s>" % key)

        for key in kwargs:
            self.root.set(key, kwargs[key])

    def setDescription(self, Description):
        assert type(Description) == str
        if self.Desc == None:
            self.Desc = etree.SubElement(self.root, 'Description')
            self.root.append(self.Desc)
        self.Desc.text = etree.CDATA(Description)

    def setParent(self, parent):
        assert etree.iselement(root) and root.tag == "DatatTypes"
        root.append(self.root)

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)

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

class Rung():
    '''
    Rung Template:
    See L5X Manual for Details,
    These members are to be used when defining a datatype.
    ----------------------------------------------------------
    For Information on this see the provided L5X Manual from Rockwell
    '''
    def __init__(self, Number, Comment = "", Content = "NOP();"):
            #Initialize Member Attributes
            assert isValidTag(TypeName)
            self.root = etree.Element("Rung")
            self.root.set("Number", str(Number))
            self.root.set("Type", "N")
            if Comment != "":
                self.Comment = etree.SubElement(self.root, 'Comment')
                self.setComment(Comment)
                self.root.append(self.Comment)

            self.rungContent = etree.SubElement(self.root, "Text")
            self.setRungContent(Content)

    def setRungContent(self, Content):
        assert type(Content) == str
        self.rungContent.text = etree.CDATA(Content)

    def setAttribute(self, **kwargs):
        for key in kwargs:
            if not key in self.root.keys():
                raise KeyError("Rung has No Attribute: <%s>" % key)

        for key in kwargs:
            self.root.set(key, kwargs[key])

    def setComment(self, Comment):
        assert type(Comment) == str
        if self.Comment == None:
            self.Comment = etree.SubElement(self.root, 'Comment')
            self.root.append(self.Comment)
        self.Comment.text = etree.CDATA(Comment)

    def setParent(self, parent):
        assert etree.iselement(root) and root.tag == "RLLContent"
        root.append(self.root)

    def getLocalRoot(self):
        return self.root

    def __str__(self):
        return etree.tostring(self.root, pretty_print = True)




# class Datatype():
#     def __init__(self,):
