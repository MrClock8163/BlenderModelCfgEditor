import os
import subprocess
import tempfile
import xml.etree.ElementTree as ET

from . import utility_data as Data

# Call CfgConvert.exe and produce config in .xml format
def CfgToXml(filePath,exePath):
    destFolder = tempfile.gettempdir()
    destName = "blendermodelcfgeditor_model_cfg_temp.xml"
    destPath = os.path.join(destFolder,destName)

    subprocess.run([exePath,"-xml","-dst",destPath,filePath])
    
    return destPath

# Parse xml to an element tree
def XmlToET(xmlPath):
    xmlFile = open(xmlPath,"r")
    xmlstring = xmlFile.read()
    xmlFile.close()

    xmlstring = xmlstring.splitlines()
    xmlstring = ["<config>"] + xmlstring[2:len(xmlstring)] + ["</config>"]
    xmlstring = "\n".join(xmlstring)

    xmlTree = ET.ElementTree(ET.fromstring(xmlstring))

    return xmlTree

# Parse element tree to custom class structure
def ETToClasses(elementClass):
    
    className = elementClass.tag.lower()
    classParent = ""
    if len(elementClass.attrib) != 0:
        classParent = elementClass.attrib["base"].lower()
    
    newClass = Data.ImportClass(className,classParent)
    
    for subelement in elementClass:
        propName = subelement.tag.lower()
        propValue = ""
        
        if "type" in subelement.attrib.keys(): # array property
            propValue = []
            for item in subelement:
                propValue.append(item.text.lower() if item.text is not None else "")
        
        elif len(subelement) != 0 or "base" in subelement.attrib.keys(): # class
            propValue = ETToClasses(subelement)
            
        elif len(subelement) == 0: # simple property
            propValue = subelement.text
            if propValue is None:
                propValue = ""
            else:
                propValue = propValue.lower()
        
        newClass.AddElement(propName,propValue)
    
    return newClass

# Read an convert model.cfg to custom class structure
def ReadConfig(filePath,exePath):
    xmlPath = CfgToXml(filePath,exePath)
    xmlTree = XmlToET(xmlPath)
    
    classTree = ETToClasses(xmlTree.getroot())
    
    return classTree

# Debug function to browse the resulting class tree
def BrowseClassTree(classTree):
    
    print(classTree.name)
    print(classTree.elements)
    
    nextElementName = ""
    while nextElementName not in classTree.elements and nextElementName != "exit":
        nextElementName = input("Open element: ")
    
    if nextElementName == "exit":
        exit()
    
    nextElement = getattr(classTree,nextElementName)
    
    if type(nextElement) is Data.ImportClass:
        BrowseClassTree(nextElement)
    elif type(nextElement) is list:
        for item in nextElement:
            print(item)
    else:
        print(nextElement)