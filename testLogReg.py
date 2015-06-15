
print(__doc__)
from sklearn import preprocessing

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




import pylab as pl
from sklearn import linear_model, datasets
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, auc

#dataMergeMini.txt
#data = [line.strip() for line in open('trainingData.csv')]
data = [line.strip() for line in open('Book12.csv')]

pod=[];
listData=[];
y=[];

for i in range(0,len(data)):
    splitData=data[i].split(';' );
    tempPod=[];
    for j in [0,1,2,3]:
    #for j in range(0,len(splitData)-1):
        #if isFloat(splitData[j]):
            tempPod.append(float(splitData[j]));
        #elif isInt(splitData[j]):
    for j in [6,10]:
            tempPod.append(int(splitData[j]));
        #else:
        #   print (splitData[j])

   # print splitData[-1]
    y.append(int(splitData[-1].strip(",")));
   # print(len(tempPod))
    pod.append(tempPod)

X=pod;
Y=y;

#ne vem ali je to pravilno skaliranje lai ne :)
#sc = preprocessing.StandardScaler().fit(X)
#X = sc.transform(X)


print (Y.count(0)*1.0/ len(Y))
#print Y

#logreg = linear_model.LogisticRegression(penalty='l1',C=2.9, solver='newton-cg')
#solver_type=L2R_LR, C=1, eps=0.01, normalization=True, bias=-1, multinomial_treatment=NValues, **kwargs)
#poskusal podatke pobrati z orange, default variables
logreg = linear_model.LogisticRegression( penalty="l2", dual=False, tol=0.0001, C=2.9,
                 fit_intercept=True, intercept_scaling=1, class_weight=None,
                 random_state=None)

# we create an instance of Neighbours Classifier and fit the data.

logreg.fit(X, Y)
Z=logreg.predict(X)
print(Z)

acc = accuracy_score(Y, Z)
print(acc)


# Compute ROC curve and area the curve
fpr, tpr, thresholds = roc_curve(Y, Z)
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


