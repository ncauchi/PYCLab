import processData

dataFile = "data\\data_1.csv"
nameFile = "testing\\aaa.txt"
startLine = 3

dat = open(nameFile, "w")
for i in range(5):
    dat.write("some_name" + str(i)+"\n")
dat.close()

processData.process(dataFile, nameFile, startLine)