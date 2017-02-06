import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from PIA.Rockwell.Types import CommonType
from PIA.Rockwell.XML.Tools import *
from PIA.Rockwell.XML.Templates import *
from PIA.Rockwell.Util.Templates import PushButton

import lxml
from lxml import etree

ARGS            = sys.argv
CONTROLLER_TAGS = []
PROGRAM_TAGS    = []

#region - Parse/Check Input Arguments
if len(ARGS) == 1:
    print "No File Path Given!"
    print "    Program Exitting..."
    print
    sys.exit()
elif len(ARGS) == 2:
    fname = ARGS[1] #Initialize FileName Variable
    if os.path.isfile(fname): #Check if file Exists
        print "Path Argument Does not Exist!"
        print "    Program Exitting..."
        print
        sys.exit()
    elif not fname.lower().endswith('.csv'):
        print "Received file is not of type *.csv"
        print "    Program Exitting..."
        print
        sys.exit()
    print "File Loading in Progress..."
    print
else:
    print "Too Many Arguments Received!"
    print "    Program Exitting..."
    print
    sys.exit()
#endregion

#region - Read in/Parse CSV File
CSV_File = open(fname, 'r', 0)
lineNum  = 0
for line in CSV_File:
    lineNum += 1
    if lineNum == 1: continue

    tagName, size, typeOption, scope, description = line.strip().split(',')

    if not "PB_" in tagName:
        tagName = "PB_" + tagName

    if not isValidTag(tagName):
        print "Invalid Tag Name Contained in CSV File"
        print "     Program Exitting..."
        print
        sys.exit()

    size = int(size)
    if  size < 0: size = 0

    typeOption == int(typeOption)
    if typeOption == 1:
        typeOption = "PB_OneButton"
    elif typeOption == 2:
        typeOption = "PB_TwoButton"
    else:
        print "Invalid Push Button Type Contained in CSV File"
        print "     Program Exitting..."
        print
        sys.exit()

    scope = int(scope)
    if scope == 0:
        CONTROLLER_TAGS.append(Tag(tagName, typeOption, Description = description, ArrayLength = size))
    if scope == 1:
        PROGRAM_TAGS.append(Tag(tagName, typeOption, Description = description, ArrayLength = size))


#endregion

#region - Generate Base XML Schema
PROJ_ATTRIBUTES = {
    "TargetName": "PB",
    "TargetType": "Routine",
    "TargetSubType": "RLL",
    "TargetClass": "Standard",
    "ContainsContext": "true"
}

print "Building Project Root..."
PROJECT = Project()
PROJECT.setAttribute(PROJ_ATTRIBUTES)

print "Building Controller Root..."
CONTROLLER = Controller("PB_Routine")
setAsContext(CONTROLLER)




#endregion
