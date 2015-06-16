__author__ = 'matejs'

#za testne potrebe je bilo potrebno zmanjsati mnozico, podatkov da vse dela brezhibno v orangu

def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False



data = [line.strip() for line in open('establishments_by_zip.dat')]

f = open('myfile.txt','w')

listData=[];
stevec=0;
for i in range(0,len(data)):

    splitData=data[i].split('|', 13 );
    tempList=[]
    for j in range(0,len(splitData)):
        if (isInt(splitData[j])):
            tempList.append(int(splitData[j]))
        else:
             tempList.append(splitData[j])

    if  tempList[1]==35006 :
        f.write(data[i]+"\n");
        print(data[i])


f.close()
