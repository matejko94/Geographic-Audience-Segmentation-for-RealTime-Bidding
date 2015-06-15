__author__ = 'matejs'


def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False


data = [line.strip() for line in open('testData.txt')]

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

#print(listData)

for i in listData:
    curr=i[1]
    currDejavnost=-1
    for j in listData:

        if j[1]==curr:
            if currDejavnost!=j[5]:
                currDejavnost=j[5]
                if j[9]==1:
                    print(j[11])

    break;