#    ---------------------------------------- HEADER ----------------------------------------
#    
#    Author: MrClock
#    Addon: Arma 3 model config editor
#    Name: Extract compiled class property
#    
#    Description:
#        Extracts a property value from a data class.
#    
#    Node inputs:
#        - 0: Name of the property to extract
#        - 1: Skeleton, Model or Animation class type input
#    
#    Return value:
#        - value of varying type or 0 if property does not exist
#    
#    ----------------------------------------------------------------------------------------

def hasParent(node):
    if len(node.inputs) == 0:
        return False
    
    if len(node.inputs[0].links) == 0:
        return False
    
    return True

result = ""

input_0 = input_0.strip()

if input_0 != "":
    result = input_1.Get(input_0)

node = input_node_1

while result == '_HIDE_' and hasParent(node):
    parentNode = node.inputs[0].links[0].from_node
    parentData = parentNode.process()
    result = parentData.Get(input_0)
    
    node = parentNode