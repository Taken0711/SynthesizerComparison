import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import tree
import graphviz
import pandas as pd
import matplotlib.pyplot as plt
import itertools


def render_tree(dt, setname, feature_names, class_names):
    dot_data = tree.export_graphviz(dt, out_file=None,
                             feature_names=feature_names,
                             class_names=class_names,
                             filled=True, rounded=True,
                             special_characters=True)

    graph = graphviz.Source(dot_data)
    graph.format = 'png'
    graph.render("tree_%s" % setname)


def make_tree(df, feature_names, clazz, set_name):
    data = df[feature_names]
    target = df[clazz]
    class_names = target.unique()

    clf = tree.DecisionTreeClassifier(max_depth=3)
    scores = cross_val_score(clf, data, target, cv=10)
    print("%s: " % set_name, scores.mean())

    dt = clf.fit(data, target)
    render_tree(dt, set_name, feature_names, class_names)

    target_pred = cross_val_predict(clf, data, target, cv=10)
    cnf_matrix = confusion_matrix(target, target_pred)

    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=class_names,
                          title='Confusion matrix for the %s dataset' % set_name)
    plt.savefig('confusion_%s.png' % set_name)
    return scores.mean()


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def main():
    ods = pd.read_csv('iris.data')
    sds = pd.read_csv('iris_syn.data')
    header = list(ods)

    f = open('iris_score.txt', 'w')

    s = make_tree(ods, header[:-1], "class", "iris_observed")
    f.write("Observed accuracy: %f\n" % s)
    s = make_tree(sds, header[:-1], "class", "iris_synthetic")
    f.write("Synthesized accuracy: %f\n" % s)

    f.close()

if __name__ == '__main__':
    main()
