# How to Read the results

## The structure of the result txt file



After calculating, you will get the results in the folder: /result/.

Here is the structure of result file:

```
index,sequence,prediction
```

**"index"** represents the index or number of the peptide, **"sequence"** represents the amino acid sequence of the peptide, and **"prediction"** represents the predicted classification result for that peptide. '1' indicates that the sequence is predicted to be an anticancer peptide; '0' indicates that the sequence is predicted to be a non-anticancer peptide.

Example:

```
index,sequence,prediction
0,FLWWLFKWAWK,1
1,FAKLAKKALAKLL,1
2,GLFDIVKKIAGHIAGSI,1
3,VNFKKLLGKLLKVVK,1
4,WKKIPKFLHLLKKF,1
5,EQCGRQAGGKLCPNNLCCSQYGWCGSSDDYCSPSKNCQSNCKGGG,1
6,EADEPLWLYKGDNIERAPTTADHPILPSIIDDVKLDPNRRYA,1
7,FVGLAKVAAHVVPAIAEHF,1
8,FAKLLAKLAKKFAL,1
9,ARSYGNGVYCNNKKCWVNRGEATQSIIGGMISGWASGLAGM,1
```

