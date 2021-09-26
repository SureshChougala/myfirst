from os import write
import xml.etree.ElementTree as ex
mytree=ex.parse("E:\Internship\Assignment_etc\employee.xml")
myroot=mytree.getroot()
for x in myroot.iter("name"):
    a=str(x.text)+" will be saved"
    x.text=str(a)
    x.set("updated", "yes")
mytree.write("new.xml")

ex.SubElement(myroot[0],"new")
for x in myroot.iter("new"):
    b="777"
    x.text=str(b)
mytree.write("new2.xml")
