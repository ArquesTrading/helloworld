FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && \
    apt-get install -y --no-install-recommends apt-utils && \    
    apt-get install -y vim && \
    apt-get install -y telnet && \
    apt-get install -y wget

RUN apt-get -y update && \
    apt-get install -y python3-pip python3-dev && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    pip3 install --upgrade pip    

COPY . /app
WORKDIR /app


RUN pip3 install -r requirements.txt

EXPOSE 5000

# ENTRYPOINT [ "python3" ]
# CMD [ "app.py"]

# ENTRYPOINT ["python3"]
# CMD ["app.py"]



###########################################################################
# FROM python

# ENV DEBIAN_FRONTEND noninteractive

# RUN apt-get -y update && \
#     apt-get install -y --no-install-recommends apt-utils && \
#     apt-get install -y vim && \
#     apt-get install -y telnet && \
#     apt-get install -y wget

# RUN python -m pip install --upgrade pip

# COPY . /app
# WORKDIR /app


# RUN pip install -r requirements.txt

# EXPOSE 5000
# # ENV FLASK_APP=app.py

# ENTRYPOINT ["python"]
# CMD ["app.py"]
###########################################################################
# ENTRYPOINT [ "flask" ]
# CMD ["run", "--host", "0.0.0.0", "-p", "5000"]



# FROM python:3.8

# RUN pip install --upgrade pip
# RUN pip install requests
# RUN pip install flask

# EXPOSE 8080

# # docker build -t helloworld .