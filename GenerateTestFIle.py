__author__ = 'matejs'
from collections import Counter
import csv
# nadomescanje manjkajocih vrednosti, kjer manjkajo vrednosti. 
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

import csv

dataTraining = [line.strip() for line in open('training_set.tsv')]
dataAllZip = [line.strip() for line in open('discreditiongZipAtributes.csv')]
dataTest=[line.strip() for line in open('test_set.tsv')]

#zipCodeClustering
#dataAllZip = [line.strip() for line in open('zipCodeClustering.csv')]
numberOfClusters=25;
dictTraining={};

setDomain=set()
setAdvartisment=set()
dataSt=0;
arrayTestData=[]
arrayTrainData=[]
#read trening data and add elements in arrayDomain and setDomain
for i in range(0,len(dataTraining)):
    splitDataTemp=dataTraining[i].split('\t');
    if len(splitDataTemp)==5:
        setDomain.add(splitDataTemp[3])
        if isInt(splitDataTemp[1]):
            setAdvartisment.add(int(splitDataTemp[1]))
        if isInt(splitDataTemp[0]) and isInt(splitDataTemp[1]) and isInt(splitDataTemp[2]):
            arrayTrainData.append([int(splitDataTemp[0]),int(splitDataTemp[1]),int(splitDataTemp[2]),splitDataTemp[3],splitDataTemp[4]])
    else:
      dataSt=dataSt+1


print(dataSt)
#read all data and add in dictionary all zips
dictMergeData={}
for data in dataAllZip:
    splitFData=data.split(",")
    tempArray=[]
    for i in range(1,len(splitFData)):
        if isFloat(splitFData[i]):
            tempArray.append(float(splitFData[i]))
        else:
            tempArray.append((splitFData[i]))
    dictMergeData[int("%d"%float(splitFData[0]))]=tempArray;

#merge all data
arrayMergeData=[];
for domain in arrayTrainData:
    #print domain
    #print dictData[domain[2]]
    if int(domain[2]) in dictMergeData:
        arrayMergeData.append(domain+dictMergeData[domain[2]])
    #else:
    #   print domain[2]
#for i in arrayMergeData:
#    print i


dictDomainCount1={}
dictDomainCount0={}
for set in setDomain:
    dictDomainCount1[set]=[0]*numberOfClusters
    dictDomainCount0[set]=[0]*numberOfClusters
dictAdvartismentCount1={}
dictAdvartismentCount0={}
for set in setAdvartisment:
    dictAdvartismentCount0[int(set)]=[0]*numberOfClusters
    dictAdvartismentCount1[int(set)]=[0]*numberOfClusters
#print setDomain




#se sprehodimo cez vse podatke
for domain in arrayMergeData:
    #Domain
    arrayDomainCount1=dictDomainCount1[domain[3]]
    arrayDomainCount0=dictDomainCount0[domain[3]]
    #Advartisment
    arrayAdvartismentCount1=dictAdvartismentCount1[int(domain[1])]
    arrayAdvartismentCount0=dictAdvartismentCount0[int(domain[1])]
    #Domain
    arrayDomainCount0[0]=arrayDomainCount0[0]+1;
    arrayAdvartismentCount0[0]=arrayAdvartismentCount0[0]+1
    arrayDomainCount0[int(domain[-1])]=arrayDomainCount0[int(domain[-1])]+1;

    arrayAdvartismentCount0[int(domain[-1])]=arrayAdvartismentCount0[int(domain[-1])]+1;

    if int(domain[0])==1:
        arrayDomainCount1[0]=arrayDomainCount1[0]+1;
        arrayDomainCount1[int(domain[-1])]=arrayDomainCount1[int(domain[-1])]+1;

        arrayAdvartismentCount1[0]=arrayAdvartismentCount1[0]+1
        arrayAdvartismentCount1[int(domain[-1])]=arrayAdvartismentCount1[int(domain[-1])]+1;


    dictAdvartismentCount0[int(domain[1])]=arrayAdvartismentCount0
    dictAdvartismentCount1[int(domain[1])]=arrayAdvartismentCount1

    dictDomainCount1[domain[3]]=arrayDomainCount1
    dictDomainCount0[domain[3]]=arrayDomainCount0


'''
10110

print "dictAdvartisment c0"
print dictAdvartismentCount0
print "dictAdvartisment c1"
print dictAdvartismentCount1

print "dictADomain c0"
print dictDomainCount0
print "dictDomain c1"
print dictDomainCount1
'''

import json

text_file = open("dictDomainCount0.txt", "w")
text_file.write(json.dumps(dictDomainCount0))
text_file.close()

text_file = open("dictDomainCount1.txt", "w")
text_file.write(json.dumps(dictDomainCount1))
text_file.close()

text_file = open("dictAdvartismentCount0.txt", "w")
text_file.write(json.dumps(dictAdvartismentCount0))
text_file.close()

text_file = open("dictAdvartismentCount1.txt", "w")
text_file.write(json.dumps(dictAdvartismentCount1))
text_file.close()

text_file = open("dictMergeData.txt", "w")
text_file.write(json.dumps(dictMergeData))
text_file.close()



ist1=0
ist2=0
ist3=0
ist4=0
ist5=0
ist6=0
ist7=0

arrayMergeFinalData=[]
i=0
for d in dataTest:
    splitDataTemp=d.split('\t');
    if len(splitDataTemp)==4 and isInt(splitDataTemp[0])and isInt(splitDataTemp[1]):
        if int(splitDataTemp[1]) in dictMergeData: #glavni z vsemi zip kodami
            domain=splitDataTemp+dictMergeData[int(splitDataTemp[1])]
            if domain[2] in dictDomainCount0:
                arrayDomainCount1=dictDomainCount1[domain[2]]
                arrayDomainCount0=dictDomainCount0[domain[2]]
            else:
                arrayDomainCount0=[0]*26
                arrayDomainCount1=[0]*26
                ist1=ist1+1

            if int(domain[0]) in dictAdvartismentCount0:
                arrayAdvartismentCount0=dictAdvartismentCount0[int(domain[0])]
                arrayAdvartismentCount1=dictAdvartismentCount1[int(domain[0])]
            else:
                arrayAdvartismentCount0=[0]*26
                arrayAdvartismentCount1=[0]*26
                ist2=ist2+1
            tempArray=domain;


            if arrayAdvartismentCount0[0]!=0:
                probabilityClickAdvartisment=arrayAdvartismentCount1[0]*1.0/arrayAdvartismentCount0[0];
            else:
                probabilityClickAdvartisment=0
                ist3=ist3+1
            if arrayAdvartismentCount0[int(domain[-1])]!=0:
                probabilityClickRegion1=arrayAdvartismentCount1[int(domain[-1])]*1.0/arrayAdvartismentCount0[int(domain[-1])]
            else:
                probabilityClickRegion1=0
                ist4=ist4+1


            if arrayDomainCount0[0]!=0:
                probabilityClickLink=arrayDomainCount1[0]*1.0/arrayDomainCount0[0]
            else:
                probabilityClickLink=0
                ist5=ist5+1

            if arrayDomainCount0[int(domain[-1])]!=0:
                probabilityClickRegion2=arrayDomainCount1[int('%d'%domain[-1])]*1.0/arrayDomainCount0[int(domain[-1])]
            else:
                probabilityClickRegion2=0
                ist6=ist6+1
            arrayMergeFinalData.append([probabilityClickAdvartisment,probabilityClickRegion1,probabilityClickLink,probabilityClickRegion2]+domain[4:len(domain)-1])#+[domain[0]])

        else:
            arrayMergeFinalData.append([0]*33)
    else:
        arrayMergeFinalData.append([0]*33)
        #print(splitDataTemp)
        ist7=ist7+1

print(str(ist1)+" "+str(ist2)+" "+str(ist3)+" "+str(ist4)+" "+str(ist5)+" "+str(ist6))
print(str(ist7))
with open('testData.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=';', lineterminator='\n')
    writer.writerows( arrayMergeFinalData)
