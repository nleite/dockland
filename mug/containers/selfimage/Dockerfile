FROM centos:7
# user that runs the process
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb
# make sure the `mongodb` user owns the data folder
RUN mkdir -p /data/db && chown -R mongodb:mongodb /data/db
# add yum.repo.d
COPY repo /etc/yum.repos.d/mongodb-org-3.2.repo

RUN cat /etc/yum.repos.d/mongodb-org-3.2.repo
#Install mongodb and dependencies
RUN set -x && yum install -y mongodb-org && yum install -y mongodb-org-server && yum install -y mongodb-org-shell
VOLUME /data/db
EXPOSE 27017
CMD ["mongod"]
