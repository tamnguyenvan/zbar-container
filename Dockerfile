FROM public.ecr.aws/lambda/python:3.9

COPY handler.py ${LAMBDA_TASK_ROOT}

COPY document.pdf ${LAMBDA_TASK_ROOT}
COPY requirements.txt .

RUN yum install poppler-utils -y
RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt &&\
    yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm &&\
    yum makecache &&\
    yum -y install zbar

CMD [ "handler.handler" ]