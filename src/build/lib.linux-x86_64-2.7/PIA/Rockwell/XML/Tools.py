try:
    import lxml
    from lxml import etree
except ImportError as e:
    print e.message

def setAsTarget(template):
    try:
        template.root.set("use", "Target")
    except:
        template.set("use", "Target")

def setAsContext(template):
    try:
        template.root.set("use", "Context")
    except:
        template.set("use", "Context")

def isValidTag(TagName):
    strCopy = TagName
    if "_" in strCopy: strCopy = strCopy.replace("_", "")
    if strCopy[0].isdigit(): return False
    return strCopy.isalnum()
