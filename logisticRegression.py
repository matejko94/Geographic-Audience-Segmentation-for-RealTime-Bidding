__author__ = 'matejs'

#logistična regresija
print(__doc__)
from sklearn import preprocessing
import numpy as np
random_state = np.random.RandomState(0)
import numpy
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
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from sklearn import linear_model, datasets
from sklearn.metrics import accuracy_score
from sklearn import svm, datasets
from sklearn.utils import shuffle
from sklearn.metrics import roc_curve, auc

#dataMergeMini.txt
#data = [line.strip() for line in open('trainingData.csv')]
data = [line.strip() for line in open('trainingData.csv')]
#dataTest = [line.strip() for line in open('testData.csv')]
#testDataMedian.csv
dataTest = [line.strip() for line in open('testDataMedian.csv')]
X_testData=[]



for i in range(0,len(dataTest)):
    splitData=dataTest[i].split(';' );
    tempPod=[];
    for j in [0,1,2,3]:
            tempPod.append(float(splitData[j]));
    for j in [4,5]:
            tempPod.append(int('%d'%float(splitData[j])));
    X_testData.append(tempPod)

pod=[];
listData=[];
y=[];

for i in range(0,len(data)):
    splitData=data[i].split(';' );
    tempPod=[];
    for j in [0,1,2,3]:
           # tempPod.append(float('%.2f'%(float(splitData[j])*10000)));
            tempPod.append(float(splitData[j]));
    for j in [6,10]:
            tempPod.append(int('%d'%float(splitData[j])));


    y.append(int(splitData[-1].strip(",")));
    pod.append(tempPod)

X=pod;





#ne vem ali je to pravilno skaliranje lai ne :)
sc = preprocessing.StandardScaler().fit(X)
X = sc.transform(X)

X_testData = sc.transform(X_testData)


X, y = shuffle(X, y, random_state=random_state)
half = int(len(data)*9.0 / 10.0)
X_train, X_test = X[:half], X[half:]
y_train, y_test = y[:half], y[half:]


print (y.count(0)*1.0/ len(y))
#print Y

#logreg = linear_model.LogisticRegression(penalty='l1',C=2.9, solver='newton-cg')
#solver_type=L2R_LR, C=1, eps=0.01, normalization=True, bias=-1, multinomial_treatment=NValues, **kwargs)
#poskusal podatke pobrati z orange, default variables
logreg = linear_model.LogisticRegression( penalty="l2", dual=False, tol=0.0001, C=2.9,
                 fit_intercept=True, intercept_scaling=1, class_weight=None,
                 random_state=None)

# we create an instance of Neighbours Classifier and fit the data.

logreg.fit(X_train, y_train)



Z=logreg.predict_proba(X_testData)
sez=[]
f = open('dataTestLog.txt','w')
for value in Z:
    f.write(str(value[1])+"\n");

f.close();



Z=logreg.predict_proba(X_test)
#print(Z)

#acc = accuracy_score(Y, Z)
#print(acc)
Zpom=[]
for i in Z:
    Zpom.append(i[1])

# Compute ROC curve and area the curve
fpr, tpr, thresholds = roc_curve(y_test, Zpom)
roc_auc = auc(fpr, tpr)
print ("Area under the ROC curve : %f" % roc_auc)

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
