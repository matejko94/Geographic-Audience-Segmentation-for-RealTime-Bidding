__author__ = 'matejs'

'''
Prva obdelava preprosto preberemo veliko datoteko in jo spravimo na manjso.
'''

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

#print(listData)
zipSet =set()
establishmentSet=set()
dataArray=[]



for i in listData:
  zipSet.add(i[1])
  if isInt(i[5]):
     if int(i[5])<100:
        establishmentSet.add(int(i[5]))
  dataArray.append(i[1])

establishmentSet=sorted(establishmentSet)
print('Zipov je')
print(len(zipSet))

print('Establishment je')
print(len(establishmentSet))
dict={};
id=0;

print('Zip to set')
for zip in zipSet:

    dict[zip]= [ 0 for i in range(0,len(establishmentSet)+1)]


estabDictId={};
for estab in establishmentSet:
    estabDictId[estab]=id
    id=id+1


print(len(listData))


print('List data')
st=0;
for j in listData:
    if j[9]==1:
        if int(j[5]) in estabDictId:
            d=dict[j[1]]
            idSez=estabDictId[int(j[5])];
            d[idSez]=j[11]
            #print(idSez)
            dict[j[1]]=d
  #  if(st%1000==0):
  #      print(st/len(listData)*100)
    st=st+1




#print (dict)

f = open('dataEstablishmentNumber2.txt','w')
for key,value in dict.iteritems():
    f.write(str(key)+", ");
    for v in value:
        f.write(str(v)+", ");
    f.write("\n");



f.close();

print establishmentSet;


