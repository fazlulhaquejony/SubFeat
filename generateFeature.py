import itertools
import numpy as np

DNAelements = 'ACGT'
RNAelements = 'ACGU'
proteinElements = 'ACDEFGHIKLMNPQRSTVWY'



def sequenceType(seqType):
    print(seqType)
    if seqType == 'DNA':
        elements = DNAelements
    else:
        if seqType == 'RNA':
            elements = RNAelements
        else:
            if seqType == 'PROTEIN' or seqType == 'PEPTIDE':
                elements = proteinElements
            else:
                elements = None

    return elements

def extract(args, X, Y):
    T = []  # All instance ...

    elements = sequenceType(args.sequenceType.upper())

    # m2 = list(itertools.product(elements, repeat=2))
    m3 = list(itertools.product(elements, repeat=3))

    def kmers(seq, k):
        v = []
        for i in range(len(seq) - k + 1):
            v.append(seq[i:i + k])

        return v

    # %%
    def diMonoKGap(x, g):  # 2___1

        m = m3
        for i in range(1, x + 1, 1):
            V = kmers(g, i + 3)
            # seqLength = len(x) - (i+2) + 1

            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print(gGap[1], end='')
                # print('-'*i, end='')
                # print(gGap[2], end=' ')
                # trackingFeatures.append(gGap[0] + gGap[1] + '-' * i + gGap[2])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[1] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                # print(C, end=',')
                t.append(C)


    # %%
    def monoDiKGap(x, g):  # 1___2

        m = m3
        for i in range(1, x + 1, 1):
            V = kmers(g, i + 3)
            # seqLength = len(x) - (i+2) + 1
            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print('-' * i, end='')
                # print(gGap[1], end='')
                # print(gGap[2], end=' ')
                # trackingFeatures.append(gGap[0] + '-' * i + gGap[1] + gGap[2])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[-2] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                # print(C, end=',')
                t.append(C)


    # %%
    # Step#2

    def pseudoKmers(sequence):
        ### k-mer ###
        ### A, AA, AAA
        k = 3
        for i in range(1, k + 1, 1):
            v = list(itertools.product(elements, repeat=i))
            # seqLength = len(x) - i + 1
            for i in v:
                # print(x.count(''.join(i)), end=',')
                t.append(sequence.count(''.join(i)) / len(sequence))

        ### --- ###

    for x, y in zip(X, Y):
        t = []
        pseudoKmers(x)
        diMonoKGap(1, x)
        monoDiKGap(1, x)

        t.append(y)
        t = np.array(t)
        T.append(t)
        ### --- ###

    return np.array(T)

