__author__ = 'matejs'

from sklearn import preprocessing
def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False
def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False
data = [line.strip() for line in open('training_set.tsv')]
pod=[];
listData=[];
y=[];
final=[]
st=0;
for i in range(0,len(data)):
    splitData=data[i].split('\t' );
    a=str(splitData[len(splitData)-1])
    final.append(splitData[:5]+[a.strip(',')])

    if st==39000:
            break;
    st=st+1
f = open('dataMergeMini.txt','w')
st=0
i=0
import csv
'''
with open('testDomain93.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    writer.writerows(final)
'''

for value in final:
    for v in value:

        f.write(str(v)+"\t");
    #f.write(str(labels[i])+", ");
    f.write("\n");
    i=i+1



f.close();

