import os

##############################
####DATA PRINTER FUNCTIONS####
##############################

class LogFormatter:
    
    @classmethod
    def Tab(cls,tabs = 0):
        return ("\t" * tabs)
        
    @classmethod
    def Log(cls,text,tabs = 0,lead = ">"):
        return (cls.Tab(tabs) + lead + " " + text.strip())
        
    @classmethod
    def LogTitle(cls,text,width = 68):
        length = width - len(text)
        start = round(length/2)
        return (("=" * start) + " " + text.strip() + " " + ("=" * (length - start)))
        
    @classmethod
    def Error(cls,text,tabs=0):
        return cls.Log("ERROR: {}".format(text),tabs,"x")

class ConfigFormatter:

    @classmethod
    def Quote(cls,string):
        return ("\"" + string + "\"")
        
    @classmethod 
    def Endl(cls):
        return "\n"
        
    @classmethod
    def TAB(cls,tabs = 0):
        return ("\t" * tabs)
    
    @classmethod
    def Comment(cls,text,tabs = 0):
        if text == "":
            return ""
        return (("\t" * tabs) + " // " + text)
        
    @classmethod
    def ValidateListItems(cls,inputList,example = ""):
        isMatching = True
        for item in inputList:
            if type(item) is not type(example):
                isMatching = False
                return False
        return True
        
    @classmethod
    def ParseStrTo(cls,value,example,delim = ","):
        
        if type(example) is float or type(example) is int:
            try:
                float(value)
            except:
                return [value,False]
            else:
                return [float(value),True]
                
        elif type(example) is str:
            return [value,True]
            
        elif type(example) is bool:
            try:
                bool(value)
            except:
                return [value,False]
            else:
                return [int(bool(value)),True]
        
        elif type(example) is list:
            tempList = [s.strip() for s in value.split(delim)]
            finalList = []
            if len(example) == 0 or type(example[0]) is str:
                finalList = tempList
            elif type(example[0]) is float or type(example[0]) is bool or type(example[0]) is int:
                isMatching = True
                for item in tempList:
                    parsingResult = cls.ParseStrTo(item,example[0])
                    finalList.append(parsingResult[0])
                    if not parsingResult[1]:
                        isMatching = False
                
                if not isMatching:
                    return [tempList,False]
                
            return [finalList,True]
            
    @classmethod
    def ClassOpen(cls,className,parentName = "",tabs = 0):
        parent = ""
        if parentName != "":
            parent = (": " + parentName)
        
        return (("\t" * tabs) + "class " + className + parent + " {")
        
    @classmethod
    def ClassClose(cls,tabs = 0):
        return (("\t" * tabs) + "};")
        
    @classmethod
    def ArrayOpen(cls,propName,tabs = 0):
        return (("\t" * tabs) + propName + "[] = {")
        
    @classmethod
    def ArrayClose(cls,tabs = 0):
        return (("\t" * tabs) + "};")
        
    @classmethod
    def Property(cls,propName,propValue,example = "",tabs = 0,inline = True,itemsPerLine = 1):
        propValuePrint = ""
        propValuePrint += (("\t" * tabs) + propName)
        
        if type(example) is float or type(example) is int:
            propValuePrint += (" = " + str(propValue) + ";")
            
        elif type(example) is bool:
            propValuePrint += (" = " + str(int(propValue)) + ";")
            
        elif type(example) is str:
            propValuePrint += (" = " + cls.Quote(str(propValue)) + ";")
            
        elif type(example) is list:
            propValuePrint += ("[] = {")
            
            if len(propValue) == 0:
                return (propValuePrint + cls.ArrayClose())
            
            exampleValue = ""
            if len(example) != 0:
                exampleValue = example[0]
                
            if not cls.ValidateListItems(propValue,exampleValue):
                return (propValuePrint + cls.ArrayClose() + cls.Comment("list items could not be validated to the uniform type (" + str(type(exampleValue)) + ")"))
            
            
            listItems = ""
            itemCounter = 0
            
            if not inline:
                propValuePrint += cls.Endl() + ("\t" * (tabs + 1))
                
            for i in range(len(propValue)):
                valueToAdd = ""
                if type(exampleValue) is str:
                    valueToAdd = cls.Quote(propValue[i])
                else:
                    valueToAdd = str(propValue[i])
                
                listItems += valueToAdd
                isLastItem = (i == len(propValue)-1)
                if not isLastItem:
                    listItems += ","
                    
                    itemCounter += 1
                if not inline and itemCounter == itemsPerLine and not isLastItem:
                    listItems += cls.Endl() + ("\t" * (tabs + 1))
                    itemCounter = 0
                    
            if inline:
                propValuePrint += (listItems + cls.ArrayClose())
            else:
                propValuePrint += (listItems + cls.Endl() + cls.ArrayClose(tabs))
        return propValuePrint

class ConfigWriter:
    
    outputDirectory = ""
    classesToPrint = []
    
    def __init__(self,outDir,toPrint):
        self.outputDirectory = outDir
        self.classesToPrint = toPrint
        
    def IsValidPath(self):
        return os.path.exists(self.outputDirectory)
        
    def IsValidList(self):
        if type(self.classesToPrint) is not list:
            return False
        elif len(self.classesToPrint) == 0:
            return False
        else:
            return True
        
    def WriteFile(self):
        if not self.IsValidList or not self.IsValidPath:
            return
        
        stringOutput = ""
        
        for cls in self.classesToPrint:
            if not callable(getattr(cls,"Print",None)):
                continue
            stringOutput += cls.Print()
            
        filePath = self.outputDirectory + "\model.cfg"
        outputFile = open(filePath,"w")
        
        print(stringOutput, file=outputFile)
        
        outputFile.close()