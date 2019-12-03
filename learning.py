import warnings
def warn(*arg,**kwargs):pass
warnings.warn= warn

from sklearn.model_selection import StratifiedKFold
cv = StratifiedKFold(n_splits=10, shuffle=True)
import modeling
from statistics import mode
import numpy as np


from sklearn.metrics import accuracy_score, \
        log_loss, \
        classification_report, \
        confusion_matrix, \
        roc_auc_score,\
        average_precision_score,\
        auc,\
        roc_curve, f1_score, recall_score, matthews_corrcoef


def classifiers(X, Y, Z, Label1, Label2, Label3, args):

    final_pred = np.array([])
    final_proba = np.array([])

    model1 = modeling.chooseModel1(args)
    model2 = modeling.chooseModel2(args)
    model3 = modeling.chooseModel3(args)

    accuray = []
    auROC = []
    avePrecision = []
    F1_Score = []
    AUC = []
    MCC = []
    Recall = []
    LogLoss = []
    mean_TPR = 0.0
    mean_FPR = np.linspace(0, 1, 100)
    Results = []  # compare algorithms
    CM = np.array([
        [0, 0],
        [0, 0],
    ], dtype=int)

    for (train_index1, test_index1), (train_index2, test_index2), (train_index3, test_index3) in zip(cv.split(X, Label1),
                                                                                                     cv.split(Y, Label2),
                                                                                                     cv.split(Z, Label3)):

        ##############################
        # For Model1
        X_train = X[train_index1]
        X_test = X[test_index1]

        LabelX_train = Label1[train_index1]
        LabelX_test = Label1[test_index1]

        model1.fit(X_train, LabelX_train)
        pred1 = model1.predict(X_test)
        X_proba = model1.predict_proba(X_test)[:, 1]


        #############################
        # For Model2
        Y_train = X[train_index2]
        Y_test = X[test_index2]

        LabelY_train = Label2[train_index2]
        LabelY_test = Label2[test_index2]       # unused

        model2.fit(Y_train, LabelY_train)
        pred2 = model2.predict(Y_test)
        Y_proba = model2.predict_proba(Y_test)[:, 1]


        #############################
        Z_train = X[train_index3]
        Z_test = X[test_index3]

        LabelZ_train = Label3[train_index3]
        LabelZ_test = Label3[test_index3]       # unused
        # SVM start
        model3.fit(Z_train, LabelZ_train)
        pred3 = model3.predict(Z_test)
        Z_proba = model3.predict_proba(Z_test)[:, 1]

        # SVM END

        ############################

        for i in range(0, len(X_test)):
            final_pred = np.append(final_pred, mode([pred1[i], pred2[i], pred3[i]]))
            # final_proba = np.append(final_proba,mode([X_proba[i], Y_proba[i], Z_proba[i]]))

        accuray.append(accuracy_score(final_pred, LabelX_test))
        CM += confusion_matrix(final_pred, LabelX_test)

        final_proba = np.append(final_proba, (X_proba + Y_proba + Z_proba) / 3)

        avePrecision.append(average_precision_score(LabelX_test, final_proba))  # auPR
        F1_Score.append(f1_score(LabelX_test, final_pred))
        MCC.append(matthews_corrcoef(LabelX_test, final_pred))
        Recall.append(recall_score(LabelX_test, final_pred))

        FPR, TPR, _ = roc_curve(LabelX_test, final_proba)
        roc_auc = auc(FPR, TPR)
        AUC.append(roc_auc)

        final_pred = np.array([])
        final_proba = np.array([])
    print("--------------------------------")
    accuray = [_ * 100.0 for _ in accuray]
    Results.append(accuray)

    print('Accuracy: {0:.4f}%\n'.format(np.mean(accuray)))
    # print('auROC: {0:.6f}'.format(np.mean(auROC)))
    # F.write('AUC: {0:.4f}\n'.format( np.mean(AUC)))
    print('auPR: {0:.4f}\n'.format(np.mean(avePrecision)))  # average_Precision
    print('F1_Score: {0:.4f}\n'.format(np.mean(F1_Score)))
    print('MCC: {0:.4f}\n'.format(np.mean(MCC)))
    # calculate AUC
    print('AUC: {0:.4f}\n'.format(np.mean(AUC)))

    TN, FP, FN, TP = CM.ravel()
    print('Recall: {0:.4f}\n'.format(np.mean(Recall)))
    print('Sensitivity: {0:.4f}%\n'.format(((TP) / (TP + FN)) * 100.0))
    print('Specificity: {0:.4f}%\n'.format(((TN) / (TN + FP)) * 100.0))
    print('Confusion Matrix:\n')
    print(str(CM) + '\n')

    # find TP FP TN FN start
    print('True positive = ', CM[0][0])
    print('False positive = ', CM[0][1])
    print('False negative = ', CM[1][0])
    print('True negative = ', CM[1][1])
    # find TP FP TN FN end


    print('_______________________________________' + '\n')


