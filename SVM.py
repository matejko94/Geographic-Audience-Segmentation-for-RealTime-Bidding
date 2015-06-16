__author__ = 'matejs'
__author__ = 'matejs'
print(__doc__)
from sklearn import preprocessing
#SVM
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



import numpy as np
import pylab as pl
from sklearn import linear_model, datasets
from sklearn.metrics import accuracy_score
from sklearn import svm, datasets
from sklearn.utils import shuffle
from sklearn.metrics import roc_curve, auc

random_state = np.random.RandomState(0)
data = [line.strip() for line in open('trainingData.csv')]
dataTest = [line.strip() for line in open('testData.csv')]
X_testData=[]
for i in range(0,len(dataTest)):
    splitData=data[i].split(';' );
    tempPod=[];
    #for j in range(0,len(splitData)-1):
    for j in [0,1,2,3,6,10]:
        if isFloat(splitData[j]):
            tempPod.append(float(splitData[j]));
        elif isInt(splitData[j]):
            tempPod.append(int(splitData[j]));
        else:
           print(splitData[j])
    X_testData.append(tempPod)

pod=[];
listData=[];
y=[];

for i in range(0,len(data)):
    splitData=data[i].split(';' );
    tempPod=[];
    #[0,1,2,3,6,10]:
    #for j in range(0,len(splitData)-1):
    for j in [0,1,2,3,6,10]:
        if isFloat(splitData[j]):
            tempPod.append(float(splitData[j]));
        elif isInt(splitData[j]):
            tempPod.append(int(splitData[j]));
        else:
           print(splitData[j])


   # print splitData[-1]
    y.append(int(splitData[-1]));
   # print(len(tempPod))
    pod.append(tempPod)

X=pod;


sc = preprocessing.StandardScaler().fit(X)
X = sc.transform(X)

X, y = shuffle(X, y, random_state=random_state)
half = int(len(data)*9.0 / 10.0)
X_train, X_test = X[:half], X[half:]
y_train, y_test = y[:half], y[half:]

# Run classifier
classifier = svm.SVC( probability=True)
print(len(X_train))
print(len(y_train))
probas = classifier.fit(X_train, y_train).predict_proba(X_test)

Z=classifier.predict_proba(X_testData)
sez=[]
f = open('dataTest.txt','w')
for value in Z:
    f.write(str(value[1])+"\n");

f.close();



Z=classifier.predict(X_test)
#print Z

acc = accuracy_score(y_test, Z)
print(acc)

fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
roc_auc = auc(fpr, tpr)
print("Area under the ROC curve : %f" % roc_auc)

# Plot ROC curve
pl.clf()
pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic example')
pl.legend(loc="lower right")
pl.show()
