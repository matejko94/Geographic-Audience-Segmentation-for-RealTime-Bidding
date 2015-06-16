__author__ = 'matejs'
import csv
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

#Diskretizacija podatkov itd

dataPopulationData =[line.strip() for line in open('2010CensusPopulationData.csv')]
dictPopulation={}
for i in range(0,len(dataPopulationData)):
    splitDataPopulation=dataPopulationData[i].split(',');
    dictPopulation[int(splitDataPopulation[0])]=[splitDataPopulation[1],splitDataPopulation[2],splitDataPopulation[3],splitDataPopulation[4],
                                                 splitDataPopulation[5],splitDataPopulation[6],splitDataPopulation[7],splitDataPopulation[8],
                                                 splitDataPopulation[9],splitDataPopulation[10],splitDataPopulation[11],splitDataPopulation[12],
                                                 splitDataPopulation[13],splitDataPopulation[14]]

zipCodeClustering = [line.strip() for line in open('zipCodeClustering.csv')]

sez=[]
for i in range(0,len(zipCodeClustering)):
    splitDataTemp=zipCodeClustering[i].split(';');
    sezTemp=[]
    for v in splitDataTemp:
        if isInt(v):
            sezTemp.append(int(v))
        elif isFloat(v):
            sezTemp.append(float(v))
    sez.append(sezTemp)

i=0
#print sez;
final=[]
sezNew=[];
for v in sez:
    temp=[];
    temp=temp+v[:3]
    if int(v[3])>int(v[4]):
        temp=temp+[1]
    elif int(v[4])>int(v[3]):
        temp=temp+[2]
    else:
        temp=temp+[3]
    temp=temp+v[5:8]
   # temp=temp.append(v[v.index(max(v[8:15]))])
    if v.index(max(v[8:15]))==8:
        temp=temp+[1]
    elif v.index(max(v[8:15]))==9:
        temp=temp+[2]
    elif v.index(max(v[8:15]))==10:
        temp=temp+[3]
    elif v.index(max(v[8:15]))==11:
        temp=temp+[4]
    elif v.index(max(v[8:15]))==12:
        temp=temp+[5]
    elif v.index(max(v[8:15]))==13:
        temp=temp+[6]
    elif v.index(max(v[8:15]))==14:
        temp=temp+[6]
    elif v.index(max(v[8:15]))==15:
        temp=temp+[7]
    else:
        temp=temp+[1];

    temp=temp+[float('%.2f'% (v[16]/5.5))]
    temp=temp+[v[17]];
    tempV=v[17:]
    tempPod=[]
    for j in range(1,len(tempV)-1):
        if isFloat(tempV[j]):
            tempPod.append(float('%.2f'% (float(tempV[j])/float(tempV[0]*1.0))))

    temp=temp+tempPod
    temp=temp+[v[len(v)-1]]
    final.append(temp);

   # if v[0]=='10110' or v[0]==10110:
   #     print v.index(max(v[8:15]))




with open('discreditiongZipAtributes.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',', lineterminator='\n')
    writer.writerows( final)
