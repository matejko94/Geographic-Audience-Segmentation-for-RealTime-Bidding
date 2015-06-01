__author__ = 'matejs'

def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

stevec=0;

data = [line.strip() for line in open('establishments_by_zip.dat')]

listData=[];
for i in range(0,len(data)):
    splitData=data[i].split('|', 13 );
    tempList=[]
    for j in range(0,len(splitData)):
        if (isInt(splitData[j])):
            tempList.append(int(splitData[j]))
        else:
             tempList.append(splitData[j])
    listData.append(tempList);


zipIdentificator={};
#print(listData)
zipSet =set()
establishmentSet=set()
dataArray=[]



for i in listData:
  zipSet.add(i[1])
  establishmentSet.add(i[5])
  dataArray.append(i[1])
  zipIdentificator[i[1]]=i[3];

print zipIdentificator

for key,value in zipIdentificator:

