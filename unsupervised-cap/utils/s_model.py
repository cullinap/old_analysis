import sklearn.metrics as metrics
from sklearn.metrics import roc_curve, auc

#roc plot

def roc_plot(fpr, tpr, roc_auc):
    # method I: plt
    import matplotlib.pyplot as plt
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()


from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

clf = GaussianNB()

X = vectorizer.fit_transform(preprocess(data['Tweet']).apply(lambda x: ', '.join(map(str, x))))
y = data['Text Label'].apply(lambda x: 1 if x=='Non-Bullying' else 0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 465)

clf.fit(X_train.toarray(),y_train)
y_pred = clf.predict(X_test.toarray())

print(classification_report(y_test, y_pred))
probs = clf.predict_proba(X_test.toarray())
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)
roc_plot(fpr,tpr,roc_auc)

from sklearn import ensemble
from sklearn.model_selection import cross_val_score

rfc = ensemble.RandomForestClassifier(n_estimators=100)

# We'll make 500 iterations, use 2-deep trees, and set our loss function.
params = {'n_estimators': 500,
          'max_depth': 2,
          'loss': 'deviance'}

# Initialize and fit the model.
ens = ensemble.GradientBoostingClassifier(**params)

ens.fit(X_train.toarray(),y_train)
y_pred = clf.predict(X_test.toarray())

print(classification_report(y_test, y_pred))
probs = ens.predict_proba(X_test.toarray())
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)
roc_plot(fpr,tpr,roc_auc)