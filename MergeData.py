__author__ = 'matejs'
__author__ = 'matejs'
from collections import Counter
import csv
dataTraining = [line.strip() for line in open('domain.csv')]
dataAllCodeMerge = [line.strip() for line in open('mergeData.csv')]

def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False


def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


numberOfClusters=26;
dictTraining={};


arrayTrainData=[]
#read trening data and add elements in arrayDomain and setDomain
for i in range(0,len(dataTraining)):
    splitDataTemp=dataTraining[i].split(',');
    if len(splitDataTemp)==6:
            arrayTrainData.append(splitDataTemp)
    else:
        print splitDataTemp


#read all data and add in dictionary all zips
dictMergeData={}
for data in dataAllCodeMerge:
    splitFData=data.split(",")
    tempArray=[]
    for i in range(0,len(splitFData)-1):
            tempArray.append(splitFData[i])
    dictMergeData["%d" %float(splitFData[len(splitFData)-1])]=tempArray;




arrayMergeFinalData=[]
for domain in arrayTrainData:


    print "aa"
    if domain[3] in dictMergeData:
       tmpArray= dictMergeData[domain[3]]
    else:
        print domain
    arrayMergeFinalData.append(domain+tmpArray)



with open('temp.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',', lineterminator='\n')
    writer.writerows( arrayMergeFinalData)