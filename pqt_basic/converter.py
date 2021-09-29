

from xml.etree.ElementTree import Element,ElementTree,SubElement,Comment,tostring
   
def indent(elem,level=0):
    i = "\n" + level*" "
    if len(elem):
       if not elem.text or not elem.text.strip():
          elem.text = i + " "
       if not elem.tail or not elem.tail.strip():
          elem.tail = i 
       for elem in elem:
          indent(elem,level+1)
       if not elem.tail or not elem.tail.strip():
          elem.tail= i 
                
    else:
         if level and(not elem.tail or not elem.tail.strip()):
            elem.tail = i
top = Element("File name")
with open("atssl_data.txt","r") as c:
    for x in c:
        splits = x.split(";")
        child = SubElement(top,"ECU Reset")
                               
        sub_child_1=SubElement(child,"Main")
        sub_child_1.text = splits[0]
        sub_child_2=SubElement(child,"Child1")
        sub_child_2.text = splits[0]
        sub_child_3=SubElement(child,"Content")
        sub_child_3.text = splits[0]
            
    indent(top)
    tree = ElementTree(top)
    
    tree.write("try.xml")