#    ---------------------------------------- HEADER ----------------------------------------
#    
#    Author: MrClock
#    Addon: Arma 3 model config editor
#    Name: Extract list item
#    
#    Description:
#        Extracts the item at the given index from a list input.
#    
#    Node inputs:
#        - 0: Index of item to extract (defaults to 0 if left empty)
#        - 1: Any list type input
#    
#    Return value:
#        - list item of any type
#    
#    ----------------------------------------------------------------------------------------

result = ""

if input_0 == "":
    input_0 = 0
else:
    input_0 = int(round(input_0,0))

if input_0 in range(len(input_1)):
    result = input_1[input_0]