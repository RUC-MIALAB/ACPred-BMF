# Easy Installation

This guide helps you install PSAIA with basic features.  We recommend building PSAIA with [Docker](#container-deployment) to avoid dependency issues. We recommend compiling PSAIA(and possibly its requirements) from the source code using the latest compiler for the best performace. You can also deploy PSAIA **without building** by [Docker](#container-deployment) . Please note that PSAIA only supports Linux; for Windows users, please consider using [WSL](https://learn.microsoft.com/en-us/windows/wsl/) or docker.

## Prerequisites

- This program needs Naccess, And it is currently not open source and needs to be downloaded from http://www.bioinf.manchester.ac.uk/naccess/ .
- This program needs Qcontacts, And it is currently open source and can be downloaded from https://github.com/brunoV/qcons.

## Requirements

Some of these packages can be installed with popular package management system, such as `apt` and `yum`:

```bash
sudo apt update && sudo apt install -y libopenblas-openmp-dev liblapack-dev libscalapack-mpi-dev libelpa-dev libfftw3-dev libcereal-dev libxc-dev g++ make cmake bc git lib32z1
```

Please refer to our [guide](https://github.com/RUC-MIALAB/PSAIA) on requirements.


## Get PSAIA source code

Of course a copy of PSAIA source code is required, which can be obtained via one of the following choices:

- Clone the whole repo with git: git clone https://github.com/RUC-MIALAB/PSAIA.git
- Clone the minimum required part of repo: `git clone https://github.com/RUC-MIALAB/PSAIA.git --depth=1`
- Get the source code of a latest version from [here](https://github.com/RUC-MIALAB/PSAIA.git)

### Update to latest release

Please check the [release page](https://github.com/RUC-MIALAB/PSAIA/releases) for the release note of a new version.

It is OK to download the new source code from beginning following the previous step.

To update your cloned git repo in-place:

```bash
git remote -v
# Check if the output contains the line below
# origin https://github.com/RUC-MIALAB/PSAIA.git (fetch)
# The remote name is marked as "origin" if you clone the repo from your own fork.

git fetch origin
git checkout v0.0.1 # Replace the tag with the latest version
git describe --tags # Verify if the tag has been successfully checked out
```



## Container Deployment

We've built a ready-for-use version of PSAIA with docker. For a quick start: pull the image, prepare the data, run container. Instructions on using the image can be accessed in [Dockerfile](../../../Dockerfile). 

