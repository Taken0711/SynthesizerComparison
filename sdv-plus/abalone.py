import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import tree
import graphviz
import pandas as pd
import matplotlib.pyplot as plt
import itertools

from sklearn.preprocessing import LabelEncoder


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
                 color="white" if cm[i, j] > thresh else "black",
                 fontsize=6)

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def main():
    ods = pd.read_csv('categorized_abalone.data')
    sds = pd.read_csv('categorized_abalone_syn.data')
    header = list(ods)

    le_sex = LabelEncoder()
    ods["Sex"] = le_sex.fit_transform(ods["Sex"])
    ods["Rings"] = ods["Rings"].astype(np.str)

    le_sex = LabelEncoder()
    sds["Sex"] = le_sex.fit_transform(sds["Sex"])
    sds["Rings"] = sds["Rings"].astype(np.str)

    f = open('abalone_score.txt', 'w')

    s = make_tree(ods, header[:-1], "Rings", "abalone_observed")
    f.write("Observed accuracy: %f\n" % s)
    s = make_tree(sds, header[:-1], "Rings", "abalone_synthetic")
    f.write("Synthesized accuracy: %f\n" % s)

if __name__ == '__main__':
    main()
