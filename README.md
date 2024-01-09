# ACPred-BMF-Manual

[![release: v0.0.1 (shields.io)](https://img.shields.io/badge/release-v0.0.1-blue)](https://github.com/RUC-MIALAB/ACPred-BMF/releases)

[![Documentation Status](https://readthedocs.org/projects/psaia/badge/?version=latest)](https://acpred-bmf.readthedocs.io/en/latest/?badge=latest)

# Table of contents

- [Introduction](#introduction)
- [Detailed Document](#detailed-document)
- [Web Server](#web-server)
- [License and credits](#license-and-credits)
- [Data](#data)
- [Requirements](#requirements)
- [Run](#run)
- [Contact](#contact)



## Introduction

**ACPred-BMF: bidirectional LSTM with multiple feature representations for explainable anticancer peptide prediction**, Bingqing Han, Nan Zhao, Chengshi Zeng, Xinqi Gong. [[Paper]](https://www.nature.com/articles/s41598-022-24404-1)

![Introduction](paper_first.png)

**Abstract:** Cancer has become a major factor threatening human life and health. Under the circumstance that traditional treatment methods such as chemotherapy and radiotherapy are not highly specific and often cause severe side effects and toxicity, new treatment methods are urgently needed. Anticancer peptide drugs have low toxicity, stronger efficacy and specificity, and have emerged as a new type of cancer treatment drugs. However, experimental identification of anticancer peptides is time-consuming and expensive, and difficult to perform in a high-throughput manner. Computational identification of anticancer peptides can make up for the shortcomings of experimental identification. In this study, a deep learning-based predictor named ACPred-BMF is proposed for the prediction of anticancer peptides. This method uses the quantitative and qualitative properties of amino acids, binary profile feature to numerical representation for the peptide sequences. The Bidirectional LSTM network architecture is used in the model, and the attention mechanism is also considered. To alleviate the black-box problem of deep learning model prediction, we visualized the automatically extracted features and used the Shapley additive explanations algorithm to determine the importance of features to further understand the anticancer peptide mechanism. The results show that our method is one of the state-of-the-art anticancer peptide predictors.

## Detailed Document

To make it more convenient to use and understand the details of ACPred-BMF, we have prepared a comprehensive documentation for ACPred-BMF. [ACPred-BMF-Docs](https://acpred-bmf.readthedocs.io/en/latest/)

## Web Server

We have made an online server where you can upload data and get results through ACPred-BMF. The server's link is provided here: [ACPredBMF-MIALAB-Server](http://mialab.ruc.edu.cn/ACPredBMFServer/)

We have also leveraged [Hugging Face – The AI community building the future.](https://huggingface.co/) to establish a server that is easier to operate. The server's link is provided here: [ACPred-BMF - a Hugging Face Space by MIALAB](https://huggingface.co/spaces/MIALAB/ACPred-BMF)

## License and credits

The project ACPred-BMF is licensed under [MIT](./LICENSE).
If you use this code in any future publications, please cite the following publications for general purpose:

- Han, B., Zhao, N., Zeng, C. *et al.* ACPred-BMF: bidirectional LSTM with multiple feature representations for explainable anticancer peptide prediction. *Sci Rep* **12**, 21915 (2022). https://doi.org/10.1038/s41598-022-24404-1
- [![doi: 10.1038/s41598-022-24404-1](https://img.shields.io/badge/DOI:10.1038/s41598022244041-blue)](https://doi.org/10.1038/s41598-022-24404-1)
- In addition, please follow [the ris file](CITATIONS.ris) to cite the methods you used.

## Data

This program needs fasta file corresponding to the peptide sequences to be predicted, you can organize the fasta files and place them in the 'data/' folder.

**Benchmark dataset:**

In this study, we use the benchmark datasets collected by Agrawal et al. in AntiCP2.0[[23]](https://www.nature.com/articles/s41598-022-24404-1#ref-CR23) for model training and result comparisons. The benchmark datasets could be downloaded from https://webs.iiitd.edu.in/raghava/anticp2/download.php. It consisted of the main dataset and the alternate dataset.

(i) In the main dataset, ACPs verified in the experiment were taken as positive samples, and anti-microbial peptides (AMPs) were taken as non-ACPs, i.e., negative samples. It contains 1722 peptides of which 861 ACPs and 861 non-ACPs (or AMPs).

(ii) In the alternate dataset, ACPs and random peptides were regarded as positive samples and negative samples, respectively. It contains 1940 peptides, including 970 experimentally validated ACPs and 970 random peptides.

## Requirements

**Recommand Dependencies：**

* Python 3.8

We have placed the required Python packages in requirements.txt. You can directly use the the command below to install them.

```
pip install -r requirements.txt
```

If you encounter any issues during the installation process, please contact us for assistance.

## Run

You can place any number of FASTA files into the data/ folder. Then, you can choose between the following two models to run:

**1.[Main_model]**: This model was developed on the main dataset, which used ACPs/AMPs as positive/negative samples.

```
bash main.sh main
```

**2.[Alternate_model]**: This model was developed on the alternate dataset, which used ACPs/random peptides as positive/negative samples.

```
bash main.sh alternative
```

Then, you will get the results in the folder: /result/

If you want to know how to read the result file, please refer to this [ACPred-BMF-result](https://acpred-bmf.readthedocs.io/en/latest/quick_start/How_to_Read_the_results.html) .


## Contact

If you have any questions, please contact with: 13168zsl@ruc.edu.cn



