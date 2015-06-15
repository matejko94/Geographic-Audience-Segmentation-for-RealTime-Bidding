__author__ = 'matejs'
import csv
def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

stevec=0;
dictZip={};
data = [line.strip() for line in open('establishments_by_zip.dat')]
#data = [line.strip() for line in open('dataa.txt')]
dataAllCodeMerge = [line.strip() for line in open('test.csv')]

listData=[];
for i in range(0,len(data)):
    splitData=data[i].split('|', 13 );
    dictZip[splitData[1]]=splitData[3];


#read all data and add in dictionary all zips
arrayMergeData=[]
for data in dataAllCodeMerge:
    splitFData=data.split(",")
    tempArray=[]
    arrayMergeData.append(["%d" %float(splitFData[len(splitFData)-1]),splitFData[len(splitFData)-2]]);

final=[]
for d in arrayMergeData:
    if d[0] in dictZip:
        final.append(d+[dictZip[d[0]]])
        print d
    #else:
     #   print d[0]


with open('mergeDataZips.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',', lineterminator='\n')
    writer.writerows( final)