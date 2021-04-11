FROM centos:centos7

RUN yum update -y && \
    yum install -y epel-release && \
    yum upgrade -y

RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"

RUN yum install make \
    readline-devel \
    zlib-devel \
    bzip2-devel \
    sqlite-devel \
    openssl-devel \
    libXext.x86_64 \
    libSM.x86_64 \
    libXrender.x86_64 \
    gcc gcc-c++ \
    libffi-devel \
    python-devel \
    git -y

ARG workdir=/opt/api
WORKDIR $workdir

RUN yum install -y https://repo.ius.io/ius-release-el7.rpm
RUN yum install -y vim python36u python36u-libs python36u-devel python36u-pip

COPY requirements.txt $workdir
RUN pip3 install --upgrade pip==21.0.1 && pip3 install -r requirements.txt && pip3 install awscli

CMD ["uwsgi", "--ini", "/opt/api/uwsgi.ini"]