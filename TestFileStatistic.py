__author__ = 'matejkoooo'

import csv
import json
import statistics

def reparseKey(dict):
    dictP={};
    for key,value in dict.items():
        dictP[int(key)]=value
    return dictP

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


text_file = open("dictDomainCount0.txt", "r")
dictDomainCount0Json=text_file.read()
text_file.close()
dictDomainCount0=json.loads(dictDomainCount0Json)
text_file = open("dictDomainCount1.txt", "r")
dictDomainCount1Json=text_file.read()
text_file.close()
dictDomainCount1=json.loads(dictDomainCount1Json)
text_file = open("dictAdvartismentCount0.txt", "r")
dictAdvartismentCount0Json=text_file.read()
text_file.close()
dictAdvartismentCount0=json.loads(dictAdvartismentCount0Json)
text_file = open("dictAdvartismentCount1.txt", "r")
dictAdvartismentCount1Json=text_file.read()
text_file.close()
dictAdvartismentCount1=json.loads(dictAdvartismentCount1Json)

text_file = open("dictMergeData.txt", "r")
dictMergeDataJson=text_file.read()
text_file.close()
dictMergeData=json.loads(dictMergeDataJson)


dictMergeData=reparseKey(dictMergeData)
dictAdvartismentCount0=reparseKey(dictAdvartismentCount0)
dictAdvartismentCount1=reparseKey(dictAdvartismentCount1)

dataTest=[line.strip() for line in open('test_set.tsv')]
stALl=len(dataTest);
arrayMergeFinalData=[]
for d in dataTest:

    probabilityClickAdvartisment=0;
    probabilityClickRegion1=0
    probabilityClickLink=0
    probabilityClickRegion2=0
    sex=0
    rase=0
    group=-1
    splitDataTemp=d.split('\t');



    st=len(splitDataTemp)
    if st>=2:
        #ce je zip je dost stvari lazjih
        if isInt(splitDataTemp[1]):
            if int(splitDataTemp[1]) in dictMergeData:
                sez=dictMergeData[int(splitDataTemp[1])]
                sex=sez[2]
                rase=sez[6]
                group=sez[-1]
            else:
                sex=2
                rase=1
                group=-1

        else:
            sex=2
            rase=1
            group=-1

        if isInt(splitDataTemp[0]):
            if int(splitDataTemp[0]) in dictAdvartismentCount0:
               arrayAdvartismentCount0=dictAdvartismentCount0[int(splitDataTemp[0])]
               arrayAdvartismentCount1=dictAdvartismentCount1[int(splitDataTemp[0])]
            else:
                arrayAdvartismentCount0=[0]*26
                arrayAdvartismentCount1=[0]*26
        else:
                arrayAdvartismentCount0=[0]*26
                arrayAdvartismentCount1=[0]*26


        if arrayAdvartismentCount0[0]!=0:
            probabilityClickAdvartisment=arrayAdvartismentCount1[0]*1.0/arrayAdvartismentCount0[0];
        else:
            probabilityClickAdvartisment=0
        if group!=-1:
            if arrayAdvartismentCount0[int(group)]!=0:
                probabilityClickRegion1=arrayAdvartismentCount1[int(group)]*1.0/arrayAdvartismentCount0[int(group)]

            else:
                if arrayAdvartismentCount0[int(group)]!=0:

                     probabilityClickRegion1=statistics.median([x/y for x, y in zip(arrayAdvartismentCount1[1:], arrayAdvartismentCount0[1:])])
                else:
                    probabilityClickRegion1=0



    if st>=3:

            if splitDataTemp[2] in dictDomainCount0:
                arrayDomainCount1=dictDomainCount1[splitDataTemp[2]]
                arrayDomainCount0=dictDomainCount0[splitDataTemp[2]]
            else:
                arrayDomainCount0=[0]*26
                arrayDomainCount1=[0]*26

            if arrayDomainCount0[0]!=0:
                probabilityClickLink=arrayDomainCount1[0]*1.0/arrayDomainCount0[0]
            else:
                probabilityClickLink=0

            if group!=-1:
                if arrayDomainCount0[int(group)]!=0:
                    probabilityClickRegion2=arrayDomainCount1[int(group)]*1.0/arrayDomainCount0[int(group)]
                else:
                    probabilityClickRegion2=0
            else:
                if arrayDomainCount0[int(group)]!=0:

                     probabilityClickRegion2=statistics.median([x/y for x, y in zip(arrayDomainCount1[1:], arrayDomainCount0[1:])])
                else:
                    probabilityClickRegion2=0

#    if st>=4:
#        if splitDataTemp[3]:
#            stTrue4=stTrue4+1


    arrayMergeFinalData.append([probabilityClickAdvartisment,probabilityClickRegion1,probabilityClickLink,probabilityClickRegion2,sex,rase])



with open('testDataMedian.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=';', lineterminator='\n')
    writer.writerows( arrayMergeFinalData)