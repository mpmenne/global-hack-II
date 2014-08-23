FROM ubuntu:12.04

RUN apt-get clean && apt-get update
RUN apt-get install -y wget python-software-properties software-properties-common curl man vim aptitude telnet git unzip slapd

RUN apt-get install -y python-pip

# mongo, python 2 .7.7, pip, 

 RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
 RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list
 RUN apt-get update && apt-get install -y mongodb-org
 RUN mkdir -p /data/db
 ADD requirements.txt /root/requirements.txt
 RUN pip install -r /root/requirements.txt
 EXPOSE 27017

 RUN apt-get update

# launch ssh
 RUN apt-get install -y openssh-server
 RUN mkdir /var/run/sshd
 RUN echo 'root:welcome' |chpasswd

# define a fake env so that the startup command works correctly
 ENV fake fake
#
 EXPOSE 22

# supervisor configuration
 ADD policy-rc.d /usr/sbin/policy-rc.d
 RUN apt-get install -y supervisor
 RUN mkdir -p /var/log/supervisor
 ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
 CMD /usr/bin/supervisord
