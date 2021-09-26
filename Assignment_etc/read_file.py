data_file=open("E:\Internship\Assignment and etc\datafile.txt","r") ##reading tada from txt file
#print(data_file.read())
for word in data_file.readlines():
    data=word.split(",")
    print(data)
    pass