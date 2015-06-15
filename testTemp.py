__author__ = 'matejkoooo'

data = [line.strip() for line in open('temp.csv')]
pod=[];
listData=[];
y=[];

for i in range(1,len(data)):
    data[i].split(',' );
    if  len(data[i].split(',' ))!=len( data[i-1].split(',' )):
        print i
      #  print  str(len(data[i].split(',' )))+' '+str(len(data[i-1].split(',' )))