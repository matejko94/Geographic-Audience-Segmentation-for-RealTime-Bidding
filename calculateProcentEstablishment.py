__author__ = 'matejs'
def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
#Izracunamo procente, raznih podatkov, z tem naj bi pridobili na testnih podatkih
data = [line.strip() for line in open('dataEstablishmentNumber2.txt')]
pod=[];
listData=[];
for i in range(0,len(data)):
    splitData=data[i].split(',' );
    tempPod=[];
    tempPod.append(splitData[0])
    tempPod.append(splitData[1])
    for j in range(2,len(splitData)):
        if isFloat(splitData[j]):
            tempPod.append(float(splitData[j].strip())/float(splitData[1].strip())*100)
    pod.append(tempPod)


#print(pod)


f = open('dataEstablishmentPercent.txt','w')
for value in pod:
    for v in value:
        if isinstance(v,str)==False :
            strf='%.2f' % v
            f.write(strf+', ');
        else:
            f.write(v+', ');

    f.write("\n");

f.close();

