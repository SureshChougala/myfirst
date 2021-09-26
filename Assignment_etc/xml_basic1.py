#PARSING

#parse key word
from os import write
import xml.etree.ElementTree as ex
mytree=ex.parse("E:\Internship\Assignment_etc\employee.xml")
myroot=mytree.getroot().tag

#fromstring()
file=open("E:\Internship\Assignment_etc\employee.xml","r")
data1=file.read()
myroot=ex.fromstring(data1)
print(myroot.tag)

#FINDINB ELEMENTG

#tag, text, attrib
for x in myroot[0]:
    print(x.tag, x.text, x.attrib)

#findall
for x in myroot.findall("row"):
    id=x.find("id").text
    name=x.find("name").text
    print(id, name)

