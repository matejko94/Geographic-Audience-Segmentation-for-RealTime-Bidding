__author__ = 'matejs'

import csv
from sklearn.cluster import KMeans
#Vse podatke dodam v eno množico
def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


dataUnemployment = [line.strip() for line in open('unemployment_by_zip.csv')]
dataDensisty = [line.strip() for line in open('population_densisty_area_by_zip.csv')]
dataEstablishment = [line.strip() for line in open('dataEstablishmentNumber2.txt')]
dataPopulationData =[line.strip() for line in open('2010CensusPopulationData.csv')]



dictEstablishment={};
dictUnemployment={}
dictDensisty={}
dictPopulation={}
dictDataCBP={}

for i in range(0,len(dataUnemployment)):
    splitDataUnemployment=dataUnemployment[i].split(',', 3 );
    try:
        dictUnemployment[int(splitDataUnemployment[0])]=[int(splitDataUnemployment[1].strip('%')),int(splitDataUnemployment[2])]
    except:
        print splitDataUnemployment

print(dictUnemployment)

for i in range(0,len(dataDensisty)):
     splitDataDensisty=dataDensisty[i].split(',', 4 );
     dictDensisty[int(splitDataDensisty[0])]=[int(splitDataDensisty[1]),float(splitDataDensisty[2]),float(splitDataDensisty[3])]

for i in range(0,len(dataPopulationData)):
    splitDataPopulation=dataPopulationData[i].split(',');
    dictPopulation[int(splitDataPopulation[0])]=[splitDataPopulation[1:14]]




for i in range(0,len(dataEstablishment)):
    splitData=dataEstablishment[i].split(', ');
    tempPod=[];
    for j in range(1,len(splitData)):
        tempPod.append(splitData[j]);
    dictEstablishment[int(splitData[0])]=(tempPod)




print len(dictEstablishment)
print len(dictUnemployment)
print len(dictDensisty)

final=[];
st=0;
for key,values in dictEstablishment.iteritems():
    finalTemp=[];
    if (key in dictDensisty) and (key in dictUnemployment) and key in dictPopulation:
        finalTemp.append(key);
        listDensisty=dictDensisty[key]
        listPopulation=dictPopulation[key];
        #print listDensisty
        # 3 stvar z seznama
        listUnemplyment=dictUnemployment[key]
        #print listUnemplyment
        # 2 stvar unimploymont
        finalTemp.append(float(listDensisty[2]));
        #3
        for i in range(0,14):
          finalTemp.append(float(listPopulation[i]));

       # print values
        finalTemp.append(float(listUnemplyment[0]));
        for i in range(0,len(values)):
           # print values[i]
            if isFloat(values[i]):
                finalTemp.append(float(values[i]));

          #  print(v)
        st=st+1;
        final.append(finalTemp);



print(st)

print(len(final))
print(len(final[0]))
print(len(final[len(final)-1]))
'''
estimators = {'k_means': KMeans(n_clusters=25)}

for name, est in estimators.items():
    est.fit(final)
    labels = est.labels_

labels.T
'''


with open('zipFinalVersion.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',', lineterminator='\n')
    writer.writerows( final)

