import argparse
import read
import generateFeature
import learning
import numpy as np


def main(args):
    print(args.sequenceType)

    X, Y = read.fetchXY(args.fasta, args.label)
    print('\nDatasets fetching done.')

    ############################################################################
    print('Features extraction begins. Be patient! The machine will take some time.')

    T = generateFeature.extract(args, X, Y)

    feature = T[:, :-1]
    label = T[:, -1]
    # print(T.shape)

    if args.sequenceType.upper() == 'PROTEIN' or args.sequenceType.upper() == 'PEPTIDE':
        X = feature[:, int(args.category1[0]):int(args.category1[1])]  # X = T[:,0:419]
        Y = feature[:, int(args.category2[0]):int(args.category2[1])]  # Y = T[:, 420]
        Z = feature[:, int(args.category3[0]):int(args.category3[1])]  # X = T[:,0:419]
    else:
        if args.sequenceType.upper() == 'DNA' or args.sequenceType.upper() == 'RNA':
            X = feature[:, int(args.category1[0]):int(args.category1[1])]  # X = T[:,0:419]
            Y = feature[:, int(args.category2[0]):int(args.category2[1])]  # Y = T[:, 420]
            Z = feature[:, int(args.category3[0]):int(args.category3[1])]  # X = T[:,0:419]
        else:
            print('Err!')
    Label1 = label
    Label2 = label
    Label3 = label
    
    learning.classifiers(X, Y, Z, Label1, Label2, Label3, args)

if __name__ == '__main__':
    ######################
    # Adding Arguments
    #####################

    p = argparse.ArgumentParser(description='Feature Geneation Tool from DNA, RNA, and Protein Sequences')

    p.add_argument('-seq', '--sequenceType', type=str, help='DNA/RNA/Potein/Peptide', default='dna')

    p.add_argument('-fa', '--fasta', type=str, help='~/FASTA.txt', default='G:\\ACP500.txt')
    p.add_argument('-la', '--label', type=str, help='~/Labels.txt', default='G:\\label.txt')

    p.add_argument('-k', '--K', type=int, help='value of k for KNN', default=5)
    p.add_argument('-cv', '--nFCV', type=int, help='Number of crossValidation', default=10)

    p.add_argument('-m1', '--model1', type=str, help='choose model1', default='LR',
                   choices=['LR', 'SVM', 'KNN', 'DT', 'SVM', 'NB', ])
    p.add_argument('-m2', '--model2', type=str, help='choose model2', default='LR',
                   choices=['LR', 'SVM', 'KNN', 'DT', 'SVM', 'NB', ])
    p.add_argument('-m3', '--model3', type=str, help='choose model3', default='LR',
                   choices=['LR', 'SVM', 'KNN', 'DT', 'SVM', 'NB', ])

    p.add_argument('-c1', '--category1', nargs='*', help='#s feature inclusive', default=[0, 8420])
    p.add_argument('-c2', '--category2', nargs='*', help='#s feature inclusive', default=[8420, 16420])
    p.add_argument('-c3', '--category3', nargs='*', help='#s feature inclusive', default=[16420, 24420])

    args = p.parse_args()

    main(args)


