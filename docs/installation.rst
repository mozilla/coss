============
Installation
============

CoSS development environment can be installed using **docker**. This way we run the web app and all it's dependencies as docker containers. `Here <https://www.docker.com/whatisdocker/>`_ you can find more info about what docker is.

************
Dependencies
************

#. You need to install docker in your system. The `installation guide <https://docs.docker.com/installation/#installation>`_ covers many operating systems but for now we only support Linux and Mac OS X. *Version required*: 1.3.1 or higher.

#. We are using an orchestration tool for docker called `docker-compose <https://docs.docker.com/compose/>`_ that helps us automate the procedure of initiating our docker containers required for development. Installation instructions can be found `in Compose's documentation <https://docs.docker.com/compose/install/>`_. *Version required*: 1.0.1 or newer.

Running Docker on Mac
#####################

Here are some notes for running Docker on Mac.

* Docker cannot run natively on Mac because it is based on a Linux kernel specific feature called LXC.
* When running docker in Mac via **boot2docker** you are running a lightweight Linux VM in Virtualbox that hosts the docker daemon and the LXC containers.
* We are running docker client in our host system that connects to the docker daemon inside boot2docker VM.
* We are using docker's *volume sharing* feature in order to share the source code with the Coss container. This is not directly supported in Mac. As a workaround boot2docker implements this feature by sharing the folder with Virtualbox first.
* The extra layer that we are adding using Virtualbox might cause some performance issues. This is a trade-off for having an easily reproducible stack without installing everything manually.

More information regarding boot2docker can be found `in the documentation <https://docs.docker.com/installation/mac/>`_.

Here are some extra steps in order to run CoSS on Mac:

#. Make sure *boot2docker* is initialized::

     $ boot2docker init

#. Make sure *boot2docker* VM is up and running::

     $ boot2docker up

#. Export *DOCKER_HOST* variables using the following command::

     $ $(boot2docker shellinit)

.. note::
   You need to make sure to run ``$(boot2docker shellinit)`` in each new shell you are using, or export it globally in order not to repeat this step every time you are working on CoSS.

*************
Building CoSS
*************

You only need to follow these steps once.

#. Fork the main `CoSS repository <https://github.com/mozilla/coss>`_.
#. Clone your fork to your local machine::

    $ git clone git@github.com:YOUR_USERNAME/coss.git coss
    (lots of output - be patient...)
    $ cd coss

#. Configure your local coss installation::

    $ cp env-dist .env

#. Start ``PostgreSQL`` container::

    $ docker-compose up -d db

#. Build the app container (this will take some time)::

    $ docker-compose build web

*****************
Populate database
*****************

You only need to follow these steps once.

#. Create the database tables and run the migrations::

    $ docker-compose run web python manage.py migrate --noinput

#. Create a superuser::

    $ docker-compose run web python manage.py createsuperuser

    #. Load http://127.0.0.1:8000 or (for Mac users only) ``<IP>:8000`` where ``<IP>`` is the one returned by ``boot2docker ip`` command.
    #. Stop the server with ``Ctrl^C``.

************
Running coss
************

#. Run coss::

    $ docker-compose up web

#. Develop!
