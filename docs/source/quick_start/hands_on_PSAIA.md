# A Quick Example

## Calculating PSAIA



In order to quickly get started with the PSAIA program, I will demonstrate the entire process using 1acb.pdb which randomly be downloaded from  [RCSB PDB: Homepage](https://www.rcsb.org/) as input.

First, put the '1acb.pdb' into data/pdb/

```
cd PSAIA/
cp ../1acb.pdb data/pdb/
```

Then, you only need to run the following order:

```
bash main.sh
```

Then, you will get the results in the folder: /result/1acb_result.txt

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
patch2
res: 108 LEU E   CENTER res: 108 LEU E
res: 106 LEU E   CENTER res: 108 LEU E
res: 50 ASN E   CENTER res: 108 LEU E
res: 107 LYS E   CENTER res: 108 LEU E
res: 85 ILE E   CENTER res: 108 LEU E
res: 84 LYS E   CENTER res: 108 LEU E
res: 109 SER E   CENTER res: 108 LEU E
res: 86 ALA E   CENTER res: 108 LEU E
res: 110 THR E   CENTER res: 108 LEU E
res: 111 ALA E   CENTER res: 108 LEU E
res: 83 LEU E   CENTER res: 108 LEU E
res: 49 GLU E   CENTER res: 108 LEU E
res: 52 VAL E   CENTER res: 108 LEU E
res: 51 TRP E   CENTER res: 108 LEU E
res: 66 VAL E   CENTER res: 108 LEU E
res: 46 LEU E   CENTER res: 108 LEU E
res: 112 ALA E   CENTER res: 108 LEU E
patch3
res: 177 LYS E   CENTER res: 180 MET E
res: 180 MET E   CENTER res: 180 MET E
res: 230 ARG E   CENTER res: 180 MET E
res: 179 ALA E   CENTER res: 180 MET E
res: 178 ASP E   CENTER res: 180 MET E
res: 228 TYR E   CENTER res: 180 MET E
res: 181 ILE E   CENTER res: 180 MET E
res: 229 ALA E   CENTER res: 180 MET E
res: 182 CYS E   CENTER res: 180 MET E
res: 176 ILE E   CENTER res: 180 MET E
res: 165 ASN E   CENTER res: 180 MET E
res: 227 VAL E   CENTER res: 180 MET E
res: 215 TRP E   CENTER res: 180 MET E
res: 101 ASN E   CENTER res: 180 MET E
res: 100 ASN E   CENTER res: 180 MET E
res: 99 ILE E   CENTER res: 180 MET E
res: 175 LYS E   CENTER res: 180 MET E
res: 98 THR E   CENTER res: 180 MET E
patch4
res: 194 ASP E   CENTER res: 141 TRP E
res: 193 GLY E   CENTER res: 141 TRP E
res: 142 GLY E   CENTER res: 141 TRP E
res: 141 TRP E   CENTER res: 141 TRP E
res: 140 GLY E   CENTER res: 141 TRP E
res: 40 HIS E   CENTER res: 141 TRP E
res: 155 LEU E   CENTER res: 141 TRP E
res: 30 GLN E   CENTER res: 141 TRP E
res: 152 PRO E   CENTER res: 141 TRP E
res: 156 GLN E   CENTER res: 141 TRP E
res: 154 ARG E   CENTER res: 141 TRP E
res: 151 THR E   CENTER res: 141 TRP E
res: 143 LEU E   CENTER res: 141 TRP E
res: 73 GLN E   CENTER res: 141 TRP E
res: 153 ASP E   CENTER res: 141 TRP E
res: 70 GLU E   CENTER res: 141 TRP E
res: 71 PHE E   CENTER res: 141 TRP E
res: 72 ASP E   CENTER res: 141 TRP E
res: 43 GLY E   CENTER res: 141 TRP E
res: 31 VAL E   CENTER res: 141 TRP E
res: 32 SER E   CENTER res: 141 TRP E
res: 67 VAL E   CENTER res: 141 TRP E
patch5
res: 234 LEU E   CENTER res: 237 TRP E
res: 237 TRP E   CENTER res: 237 TRP E
res: 236 ASN E   CENTER res: 237 TRP E
res: 235 VAL E   CENTER res: 237 TRP E
res: 238 VAL E   CENTER res: 237 TRP E
res: 240 GLN E   CENTER res: 237 TRP E
res: 239 GLN E   CENTER res: 237 TRP E
res: 241 THR E   CENTER res: 237 TRP E
res: 91 ASN E   CENTER res: 237 TRP E
res: 92 SER E   CENTER res: 237 TRP E
res: 90 LYS E   CENTER res: 237 TRP E
res: 103 ILE E   CENTER res: 237 TRP E
res: 105 LEU E   CENTER res: 237 TRP E
res: 89 PHE E   CENTER res: 237 TRP E
res: 104 THR E   CENTER res: 237 TRP E
patch6
res: 167 ASN E   CENTER res: 168 CYS E
res: 163 LEU E   CENTER res: 168 CYS E
res: 166 THR E   CENTER res: 168 CYS E
res: 165 ASN E   CENTER res: 168 CYS E
res: 169 LYS E   CENTER res: 168 CYS E
res: 168 CYS E   CENTER res: 168 CYS E
res: 164 SER E   CENTER res: 168 CYS E
res: 225 PRO E   CENTER res: 168 CYS E
res: 171 TYR E   CENTER res: 168 CYS E
res: 170 LYS E   CENTER res: 168 CYS E
res: 176 ILE E   CENTER res: 168 CYS E
res: 172 TRP E   CENTER res: 168 CYS E
res: 182 CYS E   CENTER res: 168 CYS E
res: 227 VAL E   CENTER res: 168 CYS E
patch7
res: 101 ASN E   CENTER res: 94 TYR E
res: 94 TYR E   CENTER res: 94 TYR E
res: 93 LYS E   CENTER res: 94 TYR E
res: 92 SER E   CENTER res: 94 TYR E
res: 91 ASN E   CENTER res: 94 TYR E
res: 100 ASN E   CENTER res: 94 TYR E
res: 95 ASN E   CENTER res: 94 TYR E
res: 96 SER E   CENTER res: 94 TYR E
res: 102 ASP E   CENTER res: 94 TYR E
res: 56 ALA E   CENTER res: 94 TYR E
res: 90 LYS E   CENTER res: 94 TYR E
res: 103 ILE E   CENTER res: 94 TYR E
res: 99 ILE E   CENTER res: 94 TYR E
res: 57 HIS E   CENTER res: 94 TYR E
patch8
res: 131 ALA E   CENTER res: 130 PHE E
res: 130 PHE E   CENTER res: 130 PHE E
res: 129 ASP E   CENTER res: 130 PHE E
res: 134 THR E   CENTER res: 130 PHE E
res: 162 LEU E   CENTER res: 130 PHE E
res: 181 ILE E   CENTER res: 130 PHE E
res: 132 ALA E   CENTER res: 130 PHE E
res: 230 ARG E   CENTER res: 130 PHE E
res: 210 VAL E   CENTER res: 130 PHE E
res: 201 CYS E   CENTER res: 130 PHE E
res: 203 LYS E   CENTER res: 130 PHE E
res: 232 THR E   CENTER res: 130 PHE E
res: 128 ASP E   CENTER res: 130 PHE E
res: 202 LYS E   CENTER res: 130 PHE E
res: 208 THR E   CENTER res: 130 PHE E
res: 124 PRO E   CENTER res: 130 PHE E
patch9
res: 72 ASP E   CENTER res: 71 PHE E
res: 141 TRP E   CENTER res: 71 PHE E
res: 71 PHE E   CENTER res: 71 PHE E
res: 70 GLU E   CENTER res: 71 PHE E
res: 78 GLU E   CENTER res: 71 PHE E
res: 69 GLY E   CENTER res: 71 PHE E
res: 155 LEU E   CENTER res: 71 PHE E
res: 25 GLY E   CENTER res: 71 PHE E
res: 154 ARG E   CENTER res: 71 PHE E
res: 73 GLN E   CENTER res: 71 PHE E
res: 153 ASP E   CENTER res: 71 PHE E
res: 24 PRO E   CENTER res: 71 PHE E
res: 23 VAL E   CENTER res: 71 PHE E
res: 22 ALA E   CENTER res: 71 PHE E
res: 21 GLU E   CENTER res: 71 PHE E
patch10
res: 166 THR E   CENTER res: 165 ASN E
res: 164 SER E   CENTER res: 165 ASN E
res: 165 ASN E   CENTER res: 165 ASN E
res: 163 LEU E   CENTER res: 165 ASN E
res: 230 ARG E   CENTER res: 165 ASN E
res: 182 CYS E   CENTER res: 165 ASN E
res: 176 ILE E   CENTER res: 165 ASN E
res: 168 CYS E   CENTER res: 165 ASN E
res: 169 LYS E   CENTER res: 165 ASN E
res: 167 ASN E   CENTER res: 165 ASN E
res: 181 ILE E   CENTER res: 165 ASN E
res: 180 MET E   CENTER res: 165 ASN E
res: 178 ASP E   CENTER res: 165 ASN E
res: 177 LYS E   CENTER res: 165 ASN E
patch11
res: 65 VAL E   CENTER res: 65 VAL E
res: 34 GLN E   CENTER res: 65 VAL E
res: 35 ASP E   CENTER res: 65 VAL E
res: 85 ILE E   CENTER res: 65 VAL E
res: 64 ASP E   CENTER res: 65 VAL E
res: 84 LYS E   CENTER res: 65 VAL E
res: 83 LEU E   CENTER res: 65 VAL E
res: 66 VAL E   CENTER res: 65 VAL E
res: 33 LEU E   CENTER res: 65 VAL E
res: 67 VAL E   CENTER res: 65 VAL E
res: 32 SER E   CENTER res: 65 VAL E
res: 36 LYS E   CENTER res: 65 VAL E
res: 63 SER E   CENTER res: 65 VAL E
res: 38 GLY E   CENTER res: 65 VAL E
res: 82 LYS E   CENTER res: 65 VAL E
patch12
res: 61 THR E   CENTER res: 64 ASP E
res: 64 ASP E   CENTER res: 64 ASP E
res: 62 THR E   CENTER res: 64 ASP E
res: 63 SER E   CENTER res: 64 ASP E
res: 35 ASP E   CENTER res: 64 ASP E
res: 34 GLN E   CENTER res: 64 ASP E
res: 65 VAL E   CENTER res: 64 ASP E
res: 36 LYS E   CENTER res: 64 ASP E
res: 85 ILE E   CENTER res: 64 ASP E
res: 84 LYS E   CENTER res: 64 ASP E
res: 33 LEU E   CENTER res: 64 ASP E
res: 41 PHE E   CENTER res: 64 ASP E
res: 60 VAL E   CENTER res: 64 ASP E
res: 59 GLY E   CENTER res: 64 ASP E
patch13
res: 151 THR E   CENTER res: 143 LEU E
res: 143 LEU E   CENTER res: 143 LEU E
res: 152 PRO E   CENTER res: 143 LEU E
res: 192 MET E   CENTER res: 143 LEU E
res: 191 CYS E   CENTER res: 143 LEU E
res: 142 GLY E   CENTER res: 143 LEU E
res: 141 TRP E   CENTER res: 143 LEU E
res: 150 ASN E   CENTER res: 143 LEU E
res: 144 THR E   CENTER res: 143 LEU E
res: 145 ARG E   CENTER res: 143 LEU E
res: 17 VAL E   CENTER res: 143 LEU E
res: 16 ILE E   CENTER res: 143 LEU E
res: 146 TYR E   CENTER res: 143 LEU E
res: 149 ALA E   CENTER res: 143 LEU E
patch14
res: 157 GLN E   CENTER res: 23 VAL E
res: 23 VAL E   CENTER res: 23 VAL E
res: 22 ALA E   CENTER res: 23 VAL E
res: 21 GLU E   CENTER res: 23 VAL E
res: 9 VAL E   CENTER res: 23 VAL E
res: 26 SER E   CENTER res: 23 VAL E
res: 8 PRO E   CENTER res: 23 VAL E
res: 24 PRO E   CENTER res: 23 VAL E
res: 71 PHE E   CENTER res: 23 VAL E
res: 155 LEU E   CENTER res: 23 VAL E
res: 27 TRP E   CENTER res: 23 VAL E
res: 25 GLY E   CENTER res: 23 VAL E
res: 7 GLN E   CENTER res: 23 VAL E
res: 6 ILE E   CENTER res: 23 VAL E
patch15
res: 242 LEU E   CENTER res: 242 LEU E
res: 241 THR E   CENTER res: 242 LEU E
res: 239 GLN E   CENTER res: 242 LEU E
res: 238 VAL E   CENTER res: 242 LEU E
res: 243 ALA E   CENTER res: 242 LEU E
res: 240 GLN E   CENTER res: 242 LEU E
res: 51 TRP E   CENTER res: 242 LEU E
res: 245 ASN E   CENTER res: 242 LEU E
res: 244 ALA E   CENTER res: 242 LEU E
res: 47 ILE E   CENTER res: 242 LEU E
res: 48 ASN E   CENTER res: 242 LEU E
res: 105 LEU E   CENTER res: 242 LEU E
res: 123 LEU E   CENTER res: 242 LEU E
chain  I: 
patch1
res: 25 PHE I   CENTER res: 25 PHE I
res: 21 ALA I   CENTER res: 25 PHE I
res: 24 TYR I   CENTER res: 25 PHE I
res: 23 GLU I   CENTER res: 25 PHE I
res: 22 ARG I   CENTER res: 25 PHE I
res: 26 THR I   CENTER res: 25 PHE I
res: 29 TYR I   CENTER res: 25 PHE I
res: 28 HIS I   CENTER res: 25 PHE I
res: 27 LEU I   CENTER res: 25 PHE I
res: 30 PRO I   CENTER res: 25 PHE I
res: 36 PHE I   CENTER res: 25 PHE I
res: 34 VAL I   CENTER res: 25 PHE I
res: 32 TYR I   CENTER res: 25 PHE I
res: 13 VAL I   CENTER res: 25 PHE I
res: 10 PHE I   CENTER res: 25 PHE I
res: 52 VAL I   CENTER res: 25 PHE I
res: 67 PRO I   CENTER res: 25 PHE I
res: 54 VAL I   CENTER res: 25 PHE I
patch2
res: 23 GLU I   CENTER res: 24 TYR I
res: 21 ALA I   CENTER res: 24 TYR I
res: 20 GLN I   CENTER res: 24 TYR I
res: 25 PHE I   CENTER res: 24 TYR I
res: 24 TYR I   CENTER res: 24 TYR I
res: 22 ARG I   CENTER res: 24 TYR I
res: 27 LEU I   CENTER res: 24 TYR I
res: 26 THR I   CENTER res: 24 TYR I
res: 29 TYR I   CENTER res: 24 TYR I
res: 28 HIS I   CENTER res: 24 TYR I
res: 16 LYS I   CENTER res: 24 TYR I
res: 13 VAL I   CENTER res: 24 TYR I
res: 12 GLU I   CENTER res: 24 TYR I
res: 10 PHE I   CENTER res: 24 TYR I
patch3
res: 67 PRO I   CENTER res: 10 PHE I
res: 66 VAL I   CENTER res: 10 PHE I
res: 10 PHE I   CENTER res: 10 PHE I
res: 11 PRO I   CENTER res: 10 PHE I
res: 9 SER I   CENTER res: 10 PHE I
res: 12 GLU I   CENTER res: 10 PHE I
res: 13 VAL I   CENTER res: 10 PHE I
res: 14 VAL I   CENTER res: 10 PHE I
res: 24 TYR I   CENTER res: 10 PHE I
res: 25 PHE I   CENTER res: 10 PHE I
res: 68 HIS I   CENTER res: 10 PHE I
res: 52 VAL I   CENTER res: 10 PHE I
res: 29 TYR I   CENTER res: 10 PHE I
res: 8 LYS I   CENTER res: 10 PHE I
res: 69 VAL I   CENTER res: 10 PHE I
res: 32 TYR I   CENTER res: 10 PHE I
patch4
res: 32 TYR I   CENTER res: 32 TYR I
res: 29 TYR I   CENTER res: 32 TYR I
res: 31 GLN I   CENTER res: 32 TYR I
res: 30 PRO I   CENTER res: 32 TYR I
res: 33 ASP I   CENTER res: 32 TYR I
res: 50 ASN I   CENTER res: 32 TYR I
res: 34 VAL I   CENTER res: 32 TYR I
res: 52 VAL I   CENTER res: 32 TYR I
res: 25 PHE I   CENTER res: 32 TYR I
res: 51 ARG I   CENTER res: 32 TYR I
res: 10 PHE I   CENTER res: 32 TYR I
res: 69 VAL I   CENTER res: 32 TYR I
res: 49 TYR I   CENTER res: 32 TYR I
res: 8 LYS I   CENTER res: 32 TYR I
patch5
res: 56 TYR I   CENTER res: 56 TYR I
res: 39 GLU I   CENTER res: 56 TYR I
res: 38 PRO I   CENTER res: 56 TYR I
res: 55 PHE I   CENTER res: 56 TYR I
res: 54 VAL I   CENTER res: 56 TYR I
res: 37 LEU I   CENTER res: 56 TYR I
res: 64 ASN I   CENTER res: 56 TYR I
res: 63 VAL I   CENTER res: 56 TYR I
res: 65 HIS I   CENTER res: 56 TYR I
res: 62 VAL I   CENTER res: 56 TYR I
res: 57 ASN I   CENTER res: 56 TYR I
res: 58 PRO I   CENTER res: 56 TYR I
res: 61 ASN I   CENTER res: 56 TYR I
res: 18 VAL I   CENTER res: 56 TYR I
res: 36 PHE I   CENTER res: 56 TYR I
patch6
res: 25 PHE I   CENTER res: 29 TYR I
res: 24 TYR I   CENTER res: 29 TYR I
res: 28 HIS I   CENTER res: 29 TYR I
res: 27 LEU I   CENTER res: 29 TYR I
res: 29 TYR I   CENTER res: 29 TYR I
res: 26 THR I   CENTER res: 29 TYR I
res: 30 PRO I   CENTER res: 29 TYR I
res: 32 TYR I   CENTER res: 29 TYR I
res: 31 GLN I   CENTER res: 29 TYR I
res: 34 VAL I   CENTER res: 29 TYR I
res: 10 PHE I   CENTER res: 29 TYR I
res: 12 GLU I   CENTER res: 29 TYR I
patch7
res: 16 LYS I   CENTER res: 21 ALA I
res: 20 GLN I   CENTER res: 21 ALA I
res: 19 ASP I   CENTER res: 21 ALA I
res: 22 ARG I   CENTER res: 21 ALA I
res: 21 ALA I   CENTER res: 21 ALA I
res: 18 VAL I   CENTER res: 21 ALA I
res: 17 THR I   CENTER res: 21 ALA I
res: 13 VAL I   CENTER res: 21 ALA I
res: 25 PHE I   CENTER res: 21 ALA I
res: 24 TYR I   CENTER res: 21 ALA I
res: 36 PHE I   CENTER res: 21 ALA I
res: 23 GLU I   CENTER res: 21 ALA I
res: 63 VAL I   CENTER res: 21 ALA I
res: 54 VAL I   CENTER res: 21 ALA I
patch8
res: 19 ASP I   CENTER res: 22 ARG I
res: 36 PHE I   CENTER res: 22 ARG I
res: 21 ALA I   CENTER res: 22 ARG I
res: 20 GLN I   CENTER res: 22 ARG I
res: 18 VAL I   CENTER res: 22 ARG I
res: 23 GLU I   CENTER res: 22 ARG I
res: 22 ARG I   CENTER res: 22 ARG I
res: 25 PHE I   CENTER res: 22 ARG I
res: 24 TYR I   CENTER res: 22 ARG I
res: 26 THR I   CENTER res: 22 ARG I
res: 34 VAL I   CENTER res: 22 ARG I
res: 35 TYR I   CENTER res: 22 ARG I
patch9
res: 70 GLY I   CENTER res: 51 ARG I
res: 51 ARG I   CENTER res: 51 ARG I
res: 69 VAL I   CENTER res: 51 ARG I
res: 50 ASN I   CENTER res: 51 ARG I
res: 49 TYR I   CENTER res: 51 ARG I
res: 48 ARG I   CENTER res: 51 ARG I
res: 32 TYR I   CENTER res: 51 ARG I
res: 52 VAL I   CENTER res: 51 ARG I
res: 33 ASP I   CENTER res: 51 ARG I
res: 53 ARG I   CENTER res: 51 ARG I
res: 35 TYR I   CENTER res: 51 ARG I
res: 46 ASP I   CENTER res: 51 ARG I
res: 44 THR I   CENTER res: 51 ARG I
res: 47 LEU I   CENTER res: 51 ARG I
patch10
res: 63 VAL I   CENTER res: 63 VAL I
res: 62 VAL I   CENTER res: 63 VAL I
res: 16 LYS I   CENTER res: 63 VAL I
res: 15 GLY I   CENTER res: 63 VAL I
res: 56 TYR I   CENTER res: 63 VAL I
res: 18 VAL I   CENTER res: 63 VAL I
res: 17 THR I   CENTER res: 63 VAL I
res: 64 ASN I   CENTER res: 63 VAL I
res: 55 PHE I   CENTER res: 63 VAL I
res: 14 VAL I   CENTER res: 63 VAL I
res: 65 HIS I   CENTER res: 63 VAL I
res: 13 VAL I   CENTER res: 63 VAL I
res: 67 PRO I   CENTER res: 63 VAL I
res: 54 VAL I   CENTER res: 63 VAL I
res: 36 PHE I   CENTER res: 63 VAL I
res: 21 ALA I   CENTER res: 63 VAL I
patch11
res: 25 PHE I   CENTER res: 26 THR I
res: 24 TYR I   CENTER res: 26 THR I
res: 23 GLU I   CENTER res: 26 THR I
res: 27 LEU I   CENTER res: 26 THR I
res: 26 THR I   CENTER res: 26 THR I
res: 22 ARG I   CENTER res: 26 THR I
res: 29 TYR I   CENTER res: 26 THR I
res: 30 PRO I   CENTER res: 26 THR I
res: 28 HIS I   CENTER res: 26 THR I
patch12
res: 63 VAL I   CENTER res: 55 PHE I
res: 65 HIS I   CENTER res: 55 PHE I
res: 67 PRO I   CENTER res: 55 PHE I
res: 55 PHE I   CENTER res: 55 PHE I
res: 54 VAL I   CENTER res: 55 PHE I
res: 53 ARG I   CENTER res: 55 PHE I
res: 56 TYR I   CENTER res: 55 PHE I
res: 39 GLU I   CENTER res: 55 PHE I
res: 38 PRO I   CENTER res: 55 PHE I
res: 37 LEU I   CENTER res: 55 PHE I
res: 64 ASN I   CENTER res: 55 PHE I
res: 40 GLY I   CENTER res: 55 PHE I
res: 41 SER I   CENTER res: 55 PHE I
res: 43 VAL I   CENTER res: 55 PHE I
patch13
res: 68 HIS I   CENTER res: 69 VAL I
res: 8 LYS I   CENTER res: 69 VAL I
res: 52 VAL I   CENTER res: 69 VAL I
res: 10 PHE I   CENTER res: 69 VAL I
res: 69 VAL I   CENTER res: 69 VAL I
res: 70 GLY I   CENTER res: 69 VAL I
res: 51 ARG I   CENTER res: 69 VAL I
res: 49 TYR I   CENTER res: 69 VAL I
res: 47 LEU I   CENTER res: 69 VAL I
res: 48 ARG I   CENTER res: 69 VAL I
res: 32 TYR I   CENTER res: 69 VAL I
res: 50 ASN I   CENTER res: 69 VAL I
patch14
res: 67 PRO I   CENTER res: 67 PRO I
res: 66 VAL I   CENTER res: 67 PRO I
res: 65 HIS I   CENTER res: 67 PRO I
res: 68 HIS I   CENTER res: 67 PRO I
res: 55 PHE I   CENTER res: 67 PRO I
res: 54 VAL I   CENTER res: 67 PRO I
res: 53 ARG I   CENTER res: 67 PRO I
res: 10 PHE I   CENTER res: 67 PRO I
res: 52 VAL I   CENTER res: 67 PRO I
res: 9 SER I   CENTER res: 67 PRO I
res: 25 PHE I   CENTER res: 67 PRO I
res: 63 VAL I   CENTER res: 67 PRO I
res: 13 VAL I   CENTER res: 67 PRO I
res: 14 VAL I   CENTER res: 67 PRO I
res: 11 PRO I   CENTER res: 67 PRO I
patch15
res: 63 VAL I   CENTER res: 14 VAL I
res: 14 VAL I   CENTER res: 14 VAL I
res: 13 VAL I   CENTER res: 14 VAL I
res: 12 GLU I   CENTER res: 14 VAL I
res: 11 PRO I   CENTER res: 14 VAL I
res: 67 PRO I   CENTER res: 14 VAL I
res: 10 PHE I   CENTER res: 14 VAL I
res: 15 GLY I   CENTER res: 14 VAL I
res: 16 LYS I   CENTER res: 14 VAL I
res: 64 ASN I   CENTER res: 14 VAL I
res: 65 HIS I   CENTER res: 14 VAL I
res: 66 VAL I   CENTER res: 14 VAL I

```

