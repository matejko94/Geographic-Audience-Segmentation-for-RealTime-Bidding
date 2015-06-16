__author__ = 'matejs'
from collections import Counter
import csv
#calculate domain and other thinks
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

#dataMergeMini.txt
#dataTraining = [line.strip() for line in open('dataMergeMini.txt')]
dataTraining = [line.strip() for line in open('training_set.tsv')]
dataAllZip = [line.strip() for line in open('discreditiongZipAtributes.csv')]
#zipCodeClustering
#dataAllZip = [line.strip() for line in open('zipCodeClustering.csv')]
numberOfClusters=25;
dictTraining={};

setDomain=set()
setAdvartisment=set()

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
     #  arrayTrainData.append([0,0,0,0,0])
      print splitDataTemp


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


arrayMergeFinalData=[]
i=0
for domain in arrayMergeData:

    arrayDomainCount1=dictDomainCount1[domain[3]]
    arrayDomainCount0=dictDomainCount0[domain[3]]

    arrayAdvartismentCount0=dictAdvartismentCount0[domain[1]]
    arrayAdvartismentCount1=dictAdvartismentCount1[domain[1]]
    tempArray=domain;

    probabilityClickAdvartisment=arrayAdvartismentCount1[0]*1.0/arrayAdvartismentCount0[0];
    if arrayAdvartismentCount0[int(domain[-1])]!=0:
        probabilityClickRegion1=arrayAdvartismentCount1[int(domain[-1])]*1.0/arrayAdvartismentCount0[int(domain[-1])]
    #    print str(probabilityClickRegion1)+' '+str(arrayAdvartismentCount1[int(domain[-1])])+' '+str(arrayAdvartismentCount0[int(domain[-1])])
    else:

        probabilityClickRegion1=arrayAdvartismentCount1[0]
        #print int('%d'%float(domain[-1]))
    #    print probabilityClickRegion1+' '+arrayAdvartismentCount1[int(domain[-1])]+' '+arrayAdvartismentCount0[int(domain[-1])]


    probabilityClickLink=arrayDomainCount1[0]*1.0/arrayDomainCount0[0]
    probabilityClickRegion2=arrayDomainCount1[int('%d'%domain[-1])]*1.0/arrayDomainCount0[int(domain[-1])]
#    arrayMergeFinalData.append([probabilityClickAdvartisment,probabilityClickRegion1,probabilityClickLink,probabilityClickRegion2]+domain[1:len(domain)-1]+[domain[0]])
    arrayMergeFinalData.append([probabilityClickAdvartisment,probabilityClickRegion1,probabilityClickLink,probabilityClickRegion2]+domain[5:len(domain)-1]+[domain[0]])



with open('trainingData.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=';', lineterminator='\n')
    writer.writerows( arrayMergeFinalData)
