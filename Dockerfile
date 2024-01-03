# To build this Dockerfile, run `docker build -t acpred - < Dockerfile`.


FROM python:3.9
RUN apt-get update && apt-get install -y bash
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip uninstall protobuf
RUN pip install tf-estimator-nightly==2.8.0.dev2021122109 -i https://pypi.org/simple
RUN pip install protobuf==3.19.0
RUN pip install numpy==1.22.3
RUN pip install pandas==1.3.4
RUN pip install tensorflow==2.8.0
RUN pip install scikit-learn==1.0.1
RUN pip install keras==2.8.0

# All the necessary requirements for ACPred-BMF have been installed beforehand.
RUN git clone https://github.com/RUC-MIALAB/ACPred-BMF.git --depth=1

RUN cd ACPred-BMF/ && \ 
    chmod u+x main.sh server_* *.h5
#run ACPred by choose "main" or "alternative"
CMD cd ACPred-BMF/ && bash main.sh alternative
#CMD cd ACPred-BMF/ && bash main.sh main

# To run ACPred-BMF built by this image with all available threads, execute `docker run -v <host>:<wd> -w <wd/input> acpred`.
# Replace '<host>' with the path to fasta file's directory, '<wd>' with a path to working directory.
# e.g. after cloning the repo to `$HOME` and pulling image, execute docker run -v ~/ACPred-BMF/data/:/ACPred-BMF/data/ acpred
# Then,you can download the result directory or files to the place you specify.execute 'docker cp <container id>:<wd> <host>'
# e.g. docker cp a33200255e8b:/ACPred-BMF/result/ ~/ACPred-BMF/result/.

# Please refer to https://docs.docker.com/engine/reference/commandline/run/ for more details.
