### 以centos:centos7来作为基础镜像
FROM centos:centos7

### 将dockerfile目录下的python-3.6.2.tgz复制到docker容器内
COPY Python-3.6.2.tgz /usr/local/src

### 下载编译需要用到的软件
RUN yum install -y gcc gcc-c++ autoconf automake libtool make zlib* libffi-devel

### 编译安装 python
WORKDIR /usr/local/src
RUN tar -xf Python-3.6.2.tgz
WORKDIR Python-3.6.2
RUN ./configure --prefix=/usr/local/python36 && make && make install
ENV PATH /usr/local/python36/bin:$PATH

### 创建工作目录
RUN mkdir /spider

### 将python项目复制到 /spider工作目录下
ADD main.py /spider
ADD requirements.txt /spider

### 设置 /spider 为工作目录
WORKDIR /spider

### 下载 python 项目的依赖库
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt

### 在创建个爬取的数据存放的目录，这个需要根据自己代码里面设置的目录来创建，例如：
VOLUME /data

#系统编码
ENV LANG en_US
ENV LC_ALL en_US.UTF-8

### 最后一步，运行docker镜像时运行自己的python项目
### 可以多个参数： CMD ["python3","a","main.py"]
CMD ["python3","main.py"]