#    ---------------------------------------- HEADER ----------------------------------------
#    
#    Author: MrClock
#    Addon: Arma 3 model config editor
#    Name: Extract class property
#    
#    Description:
#        Extracts a property value from a data class.
#    
#    Node inputs:
#        - 0: Name of the property to extract
#        - 1: Any class type input (Bone, Skeleton, Animation, Model)
#    
#    Return value:
#        - value of varying type or 0 if property does not exist
#    
#    ----------------------------------------------------------------------------------------

result = ""

input_0 = input_0.strip()

if input_0 != "":
    
    result = input_1.Get(input_0)