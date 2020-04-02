#  SubFeat

### [1]. Read File:
All the datasets file are in `FASTA` format which can be with `.txt` or `.fasta` extension. E.g. `anyName.txt` or  `anyName.fasta`. Please know more about the FASTA file format ([by clicking here!](https://en.wikipedia.org/wiki/FASTA_format)).

```
>1AKHA|1
KKEKSPKGKSSISPQARAFLEEVFRRKQSLNSKEKEEVAKKCGITPLQVRVWFINKRMRSK
>1AOII|1
ATCAATATCCACCTGCAGATTCTACCAAAAGTGTATTTGGAAACTGCTCCATCAAAAGGCATGTTCAGCTGAATTCAGCTGAACATGCCTTTTGATGGAGCAGTTTCCAAATACACTTTTGGTAGAATCTGCAGGTGGATATTGAT
>1B6WA|1
MELPIAPIGRIIKDAGAERVSDDARITLAKILEEMGRDIASEAIKLARHAGRKTIKAEDIELAVRRFK
```

### [2]. Feature Generation:
We initially generated feature for the

- Protein data : 24,420
- RNA date : 212
- DNA data : 212

#### Proper explanation of features: 
K is an integer number representation of feature N. For example k=3 means the number of nucleotides ranging from 1 to 3 inclusive.
kGap is an integer number representation of gap count in feature N. For example k=5 means the number of gaps ranging from 1 to 5 inclusive.

**Table 1:** Protein dataset feature extraction

| Features  | Type  | Number of features  | Feature Structure  | Explanation  |
| --------- | ----- | ------------------- | ------------------ | ------------ |
| 1 | Monomer Composition  | 20  | N | when K=1, 20 features for protein | 
| 2 | Dipeptide Composition  | 400  | NN | when K=2, 20\*20=400 features for protein | 
| 3 | Tripeptide Composition  | 8000  | NNN | when K=3, 20\*20\*20=8000 features for protein | 
| 4 | K-gapped Di-mono Composition  | 8000  | NN_N | when KGap=1, 8,000 features for protein |
| 5 | K-gapped Mono-Di Composition  | 8000  | N_NN | when KGap=1, 8,000 features for protein |
|  | **Total**  | **24,420**  |  |  |

**Table 2:**  DNA and RNA dataset feature extraction

| Features  | Type  | Number of features  | Feature Structure  | Explanation  |
| --------- | ----- | ------------------- | ------------------ | ------------ |
| 1 | Monomer Composition  | 4  | N | when K=1, 4 features for DNA/RNA | 
| 2 | Dipeptide Composition  | 16  | NN | when K=2, 4\*4=16 features for DNA/RNA | 
| 3 | Tripeptide Composition  | 64  | NNN | when K=3, 4\*4\*4=64 features for DNA/RNA | 
| 4 | K-gapped Di-mono Composition  | 64  | NN_N | when KGap=1, 64 features for DNA/RNA |
| 5 | K-gapped Mono-Di Composition  | 64  | N_NN | when KGap=1, 64 features for DNA/RNA |
|  | **Total**  | **212**  |  |  |

**Note:** When sequence becomes DNA, RNA, and Protein then N = {A,C,G,T}, N = {A,C,G,U}, and N = {A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y} respectively.

## Sub spacing(modeling): 
Here we have divided total feature space into 3 Subspaces . 
For protein dataset its full feature space c: 24,420 divided into c1: 0-8,420 ,c2: 8,420-16,420 , c3: 16,420- 24,420 .For DNA and RNA dataset its full feature space c: 212 divided into c1: 0 - 84 ,c2: 84 -148 , c3: 148 - 212 .Here anyone can give input of the c1,c2 and c3 range. The sequence can be override. But remember, the range must be  lower bound to upper bound.

### Learning/results generate:
We use four algorithm Support Vector Machine, Logistic Regression, Naive Bayes and Decision Tree. Applying these algorithms on subspace dataset, we have four different results. On this result  we have  user maximum voting algorithm to generate final result.

### How to Run Package:
You can use anyone from them.

**Test Command-line #1:**
```console
user@machine:~$ python main.py -fa protein.fasta -la proteinLabel.txt -seq protein
```

**or,**
**Test Command-line #2:** 
```console
user@machine:~$ python main.py -fa protein.fasta -la proteinLabel.txt -seq protein -f1 0 500 -f2 400 2400 -f3 1600 24420
```

**or,**
**Test Command-line #3:**
```console
user@machine:~$ python main.py -fa protein.fasta -la proteinLabel.txt -seq protein –m1 DT –m2 SVM –m3 LR -f1 0 500 -f2 400 2400 -f3 1600 24420
```

**Table 3:**  command line element
| Symbol  | Explanation  |
| ------- | ------------ |
| -fa | Fasta file with .txt or .fasta format  |
| -la | Label file with .txt extension  |
| -seq | Represent Dataset  DNA/RNA/PROTEIN  |
| -m1 | Algorithm which is used for first model it can be SVM,LR,DT,NB  |
| -m2 | Algorithm which is used for second model it can be SVM,LR,DT,NB  |
| -m3 | Algorithm which is used for third model it can be SVM,LR,DT,NB  |
| -f1 | Input of first model first input means the starting of range and second input means finished point of range which can overlap the -f2 and -f3  |
| -f2 | Input of second model first input means the starting of range and second input means finished point of range which can overlap the -f1 and -f3  |
| -f3 | Input of third model first input means the starting of range and second input means finished point of range which can overlap the -f1 and -f2  |

###  Datasets:

We have used three types of datasets in this experiment; the primary structure of protein, DNA, and RNA.

| Dataset  | Data  | Instances  | Total  | Data type  |
| -------- | ----- | ---------- | ------ | ---------- |
| HotSpots and ColdSpots(Jani et al. [1]) | HotSpots<br>ColdSpots  | 478<br>572  | **1050** | DNA | 
| Benchmark dataset for σ70 promoters(Lin et al. [2]) | Promoter<br>Non-promoter  | 741<br>1400  | **2141** | DNA | 
| Dataset PAI244(Chen et al. [3]) | Positive<br>Negative  | 125<br>119  | **244** | RNA | 
| Dataset PDB1075(Liu et al. [4]) | DNA-binding proteins<br>Non-DNA-binding proteins  | 525<br>550  | **1075** | Protein | 

### References

1. Jani, M.R., Mozlish, M.T.K., Ahmed, S., Tahniat, N.S., Farid, D.M., Shatabda, S.:
irecspot-ef: Eective sequence based features for recombination hotspot prediction.
Computers in biology and medicine 103, 17{23 (2018)
2. Lin, H., Liang, Z.Y., Tang, H., Chen, W.: Identifying sigma70 promoters with
novel pseudo nucleotide composition. IEEE/ACM transactions on computational
biology and bioinformatics (2017)
3. Chen, W., Feng, P., Ding, H., Lin, H.: Pai: Predicting adenosine to inosine editing
sites by using pseudo nucleotide compositions. Scientic reports 6, 35123 (2016)
4. Liu, B., Xu, J., Lan, X., Xu, R., Zhou, J., Wang, X., Chou, K.C.: idna-prot| dis:
identifying dna-binding proteins by incorporating amino acid distance-pairs and
reduced alphabet prole into the general pseudo amino acid composition. PloS one
9(9), e106691 (2014)











