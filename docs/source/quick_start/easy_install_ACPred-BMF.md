# Easy Installation

This guide helps you install ACPred-BMF with basic features.  We recommend building ACPred-BMF with [Docker](#container-deployment) to avoid dependency issues. We recommend compiling ACPred-BMF(and possibly its requirements) from the source code using the latest compiler for the best performace. You can also deploy ACPred-BMF **without building** by [Docker](#container-deployment) . Please note that ACPred-BMF only supports Linux; for Windows users, please consider using [WSL](https://learn.microsoft.com/en-us/windows/wsl/) or docker.

## Requirements

ACPred-BMF is developed based on Python . We recommend using **Python version 3.8.12 or higher**. Below are the prerequisite Python packages with their versions required for this software.

```bash
protobuf == 3.19.0
numpy == 1.22.3
pandas == 1.3.4
tensorflow == 2.8.0
scikit-learn == 1.0.1
keras == 2.8.0
```

We provide a requirements.txt in our [GitHub repository](https://github.com/RUC-MIALAB/ACPred-BMF.git) which you can use with the command below to obtain these packages directly. 

```
pip install -r requirements.txt
```

However, if you prefer to skip the process of configuring these packages, we recommend using [Docker](#container-deployment).

Please refer to our [guide](https://github.com/RUC-MIALAB/ACPred-BMF) on requirements.


## Get ACPred-BMF source code

Of course a copy of ACPred-BMF source code is required, which can be obtained via one of the following choices:

- Clone the whole repo with git: git clone https://github.com/RUC-MIALAB/ACPred-BMF.git
- Clone the minimum required part of repo: `git clone https://github.com/RUC-MIALAB/ACPred-BMF.git --depth=1`
- Get the source code of a latest version from [here](https://github.com/RUC-MIALAB/ACPred-BMF.git)

### Update to latest release

Please check the [release page](https://github.com/RUC-MIALAB/ACPred-BMF/releases) for the release note of a new version.

It is OK to download the new source code from beginning following the previous step.

To update your cloned git repo in-place:

```bash
git remote -v
# Check if the output contains the line below
# origin https://github.com/RUC-MIALAB/ACPred-BMF.git (fetch)
# The remote name is marked as "origin" if you clone the repo from your own fork.

git fetch origin
git checkout v0.0.1 # Replace the tag with the latest version
git describe --tags # Verify if the tag has been successfully checked out
```



## Container Deployment

We've built a ready-for-use version of ACPred-BMF with dockerfile. For a quick start: download the dockerfile, prepare the data, run container. Instructions on using the image can be accessed in [Dockerfile](../../../Dockerfile). 

