import xml.etree.ElementTree as xml
file=open("E:\Internship\Assignment_etc\datafile.txt", "r")
nfile=file.readlines()
root=xml.Element("ATSSL")
for word in nfile:
    data=word.strip().split(",")
    print(data)
    d1=xml.Element(str(data[0]))
    root.append(d1)
    data.remove(data[0])
    i=0
    for cont in data:
        i=i+1
        if i%2!=0:
            d2=xml.SubElement(d1,str(cont))
            
        else:
            d2.text=str(cont)

tree=xml.ElementTree(root)
tree.write("data_xmlnew.xml")