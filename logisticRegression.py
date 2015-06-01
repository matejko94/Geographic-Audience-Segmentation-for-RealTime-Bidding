__author__ = 'matejs'
print(__doc__)
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
# Code source: Gal Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from sklearn import linear_model, datasets
from sklearn.metrics import accuracy_score
from sklearn import svm, datasets
from sklearn.utils import shuffle
from sklearn.metrics import roc_curve, auc


data = [line.strip() for line in open('dataforSVM3.txt')]
pod=[];
listData=[];
y=[];

for i in range(0,len(data)):
    splitData=data[i].split(', ' );
    tempPod=[];
    for j in range(0,len(splitData)-1):
        if isFloat(splitData[j]):
            tempPod.append(float(splitData[j]));
        elif isInt(splitData[j]):
            tempPod.append(int(splitData[j]));


   # print splitData[-1]
    y.append(float(splitData[-1].strip(",")));
   # print(len(tempPod))
    pod.append(tempPod)

X=pod;
Y=y;

sc = preprocessing.StandardScaler().fit(X)
X = sc.transform(X)


print Y.count(0)*1.0/ len(Y)
#print Y
h = .02  # step size in the mesh

logreg = linear_model.LogisticRegression(C=2.0)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)



# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
#x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
#y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
#xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
#Z=logreg.predict_proba(X)
Z=logreg.predict(X)
print Z

acc = accuracy_score(Y, Z)
print acc


# Compute ROC curve and area the curve
fpr, tpr, thresholds = roc_curve(Y, Z)
roc_auc = auc(fpr, tpr)
print "Area under the ROC curve : %f" % roc_auc

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
'''
# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())

plt.show()
'''