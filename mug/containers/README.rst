Docker Machine
==============

Let's start by creating an isolated environment for my docker experiments
.. code-block:: bash

  docker-machine create mug --driver=virtualbox
  eval "$(docker-machine env mug)"

This will create a virtual machine using virtualbox to launch docker
Docker does not have yet an native implementation for MacOSX or Windows.

Docker
======

images
------
Make sure you have pulled the correct image
.. code-block:: bash

  docker pull mongo:latest

To run a simple node is as simple as the following:
.. code-block:: bash

  docker run -p "30001:27017" -d mongo:3.2  mongod
  mongo --host DOCKER_VM_IP:30001

If we want to use our own docker image we can build one
.. code-block:: bash

  > cat selfimage/Dockerfile
  FROM centos:7
  # user that runs the process
  RUN groupadd -r mongodb && useradd -r -g mongodb mongodb
  # make sure the `mongodb` user owns the data folder
  RUN mkdir -p /data/db && chown -R mongodb:mongodb /data/db
  # add yum.repo.d
  COPY repo /etc/yum.repos.d/mongodb-org-3.2.repo
  #Install mongodb and dependencies
  RUN set -x && yum install -y mongodb-org && yum install -y mongodb-org-server && yum install -y mongodb-org-shell
  VOLUME /data/db
  EXPOSE 27017
  CMD ["mongod"]

  > docker build -t localmongo .
.. note::

  Don't forget that this is mere simplification and the current docker hub images
  are pretty good and well maintained!
  https://github.com/docker-library/mongo

After we have created our image we can now raise a container using such image

.. code-block::

  #instruction  port mapping   container name    image name
  docker run -p 30001:27017 --name local  -d localmongo


We can then build our own image
.. code-block:: sh

  docker build .

.. note:

  - we are not deactivating NUMA and applying other optimizations that might be relevant for MongoDB deployments

Persistency
===========

A few things we should start considering from this point onwards.
The beauty of containers is not that you can "just" run processes in an
isolated fashion with low resource allocation,
is mostly around the small complexity that it offers to run systems at scale.
So if we need to scale a service fast we just need to spin-up a few containers.

Now, when we are in a stateless scenario, this is pretty simple,
run a few instances, have some configuration and boot up the same software. Easy.
But in a state-full scenario, databases and persistency requirements,
we need to think of how do we make sure that the work we are doing is not going
to disappear once the container is turn off.

Docker Named Volumes
--------------------

Don't solve everything but help quite a bit



Compose
=======

Compose allow us to set different containers and linked them into deployment stacks.
Today we are just going to use it for a simple replica set setup.

For these we have a few different options.
Let's have a look on how to manage containers with `docker-compose`

cat replicaset/docker-compose.yml




Things that will help!
----------------------
- https://github.com/docker/compose/issues/2434
- https://github.com/docker/machine/issues/179
- https://github.com/docker-library/mongo/issues/30

Kubernetes
==========
