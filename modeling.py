# scikit-learn :
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

def chooseModel1(args):
    # 1. using LR:
    if args.model1 == 'LR':
        model1 = LogisticRegression()
        # print('LR ', end='')

    # 2. using KNN:
    if args.model1 == 'KNN':
        model1 = KNeighborsClassifier(n_neighbors=args.K)
        # print('KNN ', end='')

    # 3. using DT:
    if args.model1 == 'DT':
        model1 = DecisionTreeClassifier()
        # print('DT ', end='')

    # 4. using SVM:
    if args.model1 == 'SVM':
        model1 = SVC(probability=True)
        # print('SVM ', end='')

    # 5. using NB:
    if args.model1 == 'NB':
        model1 = GaussianNB()
        # print('NB ', end='')
    return model1

def chooseModel2(args):
    # 1. using LR:
    if args.model2 == 'LR':
        model2 = LogisticRegression()
        # print('LR ', end='')

    # 2. using KNN:
    if args.model2 == 'KNN':
        model2 = KNeighborsClassifier(n_neighbors=args.K)
        # print('KNN ', end='')

    # 3. using DT:
    if args.model2 == 'DT':
        model2 = DecisionTreeClassifier()
        # print('DT ', end='')

    # 4. using SVM:
    if args.model2 == 'SVM':
        model2 = SVC(probability=True)
        # print('SVM ', end='')

    # 5. using NB:
    if args.model2 == 'NB':
        model2 = GaussianNB()
        # print('NB ', end='')
    return model2

def chooseModel3(args):
    # 1. using LR:
    if args.model3 == 'LR':
        model3 = LogisticRegression()
        # print('LR ', end='')

    # 2. using KNN:
    if args.model3 == 'KNN':
        model3 = KNeighborsClassifier(n_neighbors=args.K)
        # print('KNN ', end='')

    # 3. using DT:
    if args.model3 == 'DT':
        model3 = DecisionTreeClassifier()
        # print('DT ', end='')

    # 4. using SVM:
    if args.model3 == 'SVM':
        model3 = SVC(probability=True)
        # print('SVM ', end='')

    # 5. using NB:
    if args.model3 == 'NB':
        model3 = GaussianNB()
        # print('NB ', end='')
    return model3




