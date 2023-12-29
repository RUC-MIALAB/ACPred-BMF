# How to Read the results

## The structure of the result txt file



After calculating, you will get the results in the folder: /result/.

Here is the structure of result file:

```
chain  {id}: 
patch {number}

Each line consists of 6 elements:
1、Patch's residue number            2、Residue's name              3、Residue's chain ID
4、Patch's center residue number     5、Center residue's name       4、Center residue's chain ID
```

Example:

```
chain  E: 
patch1
res: 85 ILE E   CENTER res: 85 ILE E
res: 64 ASP E   CENTER res: 85 ILE E
res: 84 LYS E   CENTER res: 85 ILE E
res: 62 THR E   CENTER res: 85 ILE E
res: 109 SER E   CENTER res: 85 ILE E
res: 108 LEU E   CENTER res: 85 ILE E
res: 107 LYS E   CENTER res: 85 ILE E
res: 86 ALA E   CENTER res: 85 ILE E
res: 87 LYS E   CENTER res: 85 ILE E
res: 61 THR E   CENTER res: 85 ILE E
res: 65 VAL E   CENTER res: 85 ILE E
res: 106 LEU E   CENTER res: 85 ILE E
res: 83 LEU E   CENTER res: 85 ILE E
res: 66 VAL E   CENTER res: 85 ILE E
res: 60 VAL E   CENTER res: 85 ILE E
res: 88 VAL E   CENTER res: 85 ILE E
res: 33 LEU E   CENTER res: 85 ILE E
```

##### Remark : You can modify the output format of the result in work/sort_patch.sh.