import csv


def process(dataFile, nameFile, startLine):
    dat = open(dataFile, "r")
    names = open(nameFile, "r")
    file = csv.reader(dat)



    #skip first n lines
    for i in range( startLine ):
        next(file)



    sampleNum = 0
    currTime = -99
    prevTime = 0
    samp = None
    output = None

    print("Beginning Data Processing")

    for line in file:
        prevTime = currTime
        currTime = float(line[1])

        if currTime - prevTime > 1 :
            if samp != None:
                samp.close()
            sampleNum += 1
            name = "data\\" + names.readline()[:-1] + ".csv"

            print("Processing Data of Sample" + name)
            samp = open(name, "w")
            output = csv.writer(samp, lineterminator="\n")
            output.writerow(["Time", "Distance", "Force"])
        
        output.writerow([currTime, line[2], line[3]])

    print("Data Processing Complete")

