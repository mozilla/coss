#!/bin/bash
set -e

export MESOS_CLUSTER=True
export `cat env-dist | sed s/\ =\ /=/ | grep -v ^\# | xargs`
python manage.py collectstatic --noinput
python manage.py compress --force
