#region - Imports
import sys, os, shutil
from PIA.Rockwell.Types import CommonType
from PIA.Rockwell.XML.Tools import *
from PIA.Rockwell.XML.Templates import *
from PIA.Rockwell.Util.Templates.Datatypes.PushButton import *

import lxml
from lxml import etree
#endregion

#region - Global Variables
ARGS            = sys.argv
CONTROLLER_TAGS = []
PROGRAM_TAGS    = []
RUNGS           = []
#endregion

#region - Help
HELP = '''
Usage Pattern:
> python BuildPBRoutine.py [path/to/input/file.csv] [path/to/output/file.L5X]

Usage Notes:
- If no output file is given, then the output will be written to the current
    current directory with filename 'PB.L5X'
- Input filetype MUST be of type '*.csv'
- Output filetype MUST be of type '*.L5X'
- All Arguments are Case Sensitive

Example 1:
$Reads Data from '.pb.csv' and writes to 'root/Desktop/Station5_PB.L5X'
> python BuildPBRoutine.py ./pb.csv /root/Desktop/Station5_PB.L5X

Example 2:
$Reads Data from '.pb.csv' and writes to './PB.L5X'
> python BuildPBRoutine.py ./pb.csv
'''
#endregion

#region - Parse/Check Input Arguments
if len(ARGS) == 1:
    print(HELP)
    sys.exit()
elif len(ARGS) == 2:
    fname = ARGS[1] #Initialize FileName Variable
    oname = os.getcwd() + "/PB.L5X"
    if not os.path.isfile(fname): #Check if file Exists
        print "Path Argument %s Does not Exist!" % (fname)
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
elif len(ARGS) == 3:
    fname = ARGS[1] #Initialize FileName Variable
    oname = ARGS[2]
    if not os.path.isfile(fname): #Check if file Exists
        print "Path Argument %s Does not Exist!" % (fname)
        print "    Program Exitting..."
        print
        sys.exit()
    elif not fname.lower().endswith('.csv'):
        print "Received file is not of type *.csv"
        print "    Program Exitting..."
        print
        sys.exit()
    elif not oname.endswith('.L5X'):
        print "Received file is not of type *.L5X"
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
LINE_NUM, RUNG_NUM  = 0, 0
for line in CSV_File:
    LINE_NUM += 1
    if LINE_NUM == 1: continue

    tagName, typeOption, scope, description = line.strip().split(',')

    if not "PB_" in tagName:
        tagName = "PB_" + tagName

    if not isValidTag(tagName):
        print "Invalid Tag Name Contained in CSV File"
        print "     Program Exitting..."
        print
        sys.exit()

    size = 0

    typeOption = int(typeOption)
    if typeOption == 1:
        typeOption = "PB_OneButton"
        RUNGS.append(Rung(RUNG_NUM,     Comment = description + " -- Push Button",
                     Content = "AFI()OTE(" + tagName + ".Visibility);"))
        RUNGS.append(Rung(RUNG_NUM + 1,
                     Content = "XIC(" + tagName + ".Push)OTE(" + tagName + ".State);"))
        RUNGS.append(Rung(RUNG_NUM + 2,
                     Content = "XIC(" + tagName + ".State)OTE(" + tagName + ".Ind);"))
        RUNG_NUM += 3
    elif typeOption == 2:
        typeOption = "PB_TwoButton"
        RUNGS.append(Rung(RUNG_NUM,     Comment = description + " -- Push Button A",
                     Content = "AFI()OTE(" + tagName + ".ButtonA.Visibility);"))
        RUNGS.append(Rung(RUNG_NUM + 1,
                     Content = "XIC(" + tagName + ".ButtonA.Push)OTE(" + tagName + ".ButtonA.State);"))
        RUNGS.append(Rung(RUNG_NUM + 2,
                     Content = "XIC(" + tagName + ".ButtonA.State)OTE(" + tagName + ".ButtonA.Ind);"))
        RUNGS.append(Rung(RUNG_NUM + 3,     Comment = description + " -- Push Button B",
                     Content = "AFI()OTE(" + tagName + ".ButtonB.Visibility);"))
        RUNGS.append(Rung(RUNG_NUM + 4,
                     Content = "XIC(" + tagName + ".ButtonB.Push)OTE(" + tagName + ".ButtonB.State);"))
        RUNGS.append(Rung(RUNG_NUM + 5,
                     Content = "XIC(" + tagName + ".ButtonB.State)OTE(" + tagName + ".ButtonB.Ind);"))
        RUNG_NUM += 6
    else:
        print "Invalid Push Button Type Contained in CSV File."
        print " -> Expected 1 or 2, Got %s" % str(typeOption)
        print "     Program Exitting..."
        print
        sys.exit()

    scope = int(scope)
    if scope == 0:
        CONTROLLER_TAGS.append(Tag(tagName, typeOption, UseRadix = False, Description = description, ArrayLength = size))
    if scope == 1:
        PROGRAM_TAGS.append(Tag(tagName, typeOption, UseRadix = False, Description = description, ArrayLength = size))
#endregion

#region - Generate L5X Schema
print "---------INITIALIZING L5X SCHEMA---------"
print "Building Project Root..."
PROJECT = Project()
PROJECT.setAttribute({
    "TargetName": "PB",
    "TargetType": "Routine",
    "TargetSubType": "RLL",
    "TargetClass": "Standard",
    "ContainsContext": "true"
})

print "Building Controller Root..."
CONTROLLER = Controller("PB_Routine_Controller")
setAsContext(CONTROLLER)
PROJECT.setController(CONTROLLER)

print "Building Relevant Push Button Datatypes..."
CONTROLLER.addDatatype(PB_OneButton())
CONTROLLER.addDatatype(PB_TwoButton())
setAsContext(CONTROLLER.Datatypes)

if not CONTROLLER_TAGS == None:
    print "Building Controller Scope Tags..."
    for tag in CONTROLLER_TAGS:
        CONTROLLER.addTag(tag)
    setAsContext(CONTROLLER.Tags)

print "Building Program Root..."
PROGRAM = Program("PB_Routine_Program")
setAsContext(PROGRAM)
CONTROLLER.addProgram(PROGRAM)

if not PROGRAM_TAGS == None:
    print "Building Program Scope Tags..."
    for tag in PROGRAM_TAGS:
        PROGRAM.addTag(tag)
    setAsContext(PROGRAM.Tags)

print "Building Routine Root..."
ROUTINE = Routine("PB")
setAsTarget(ROUTINE)
PROGRAM.addRoutine(ROUTINE)
setAsContext(PROGRAM.Routines)

print "Building Rungs..."
for rung in RUNGS:
    ROUTINE.addRung(rung)
print "---------DONE BUILDING L5X SCHEMA---------"
print
#endregion

#region - Package/Export as L5X File
print "Writing to Output File: %s ..." % (oname)
print
PROJECT.writeToFile(oname)
#endregion
