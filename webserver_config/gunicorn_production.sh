#!/bin/bash
set -e
NUM_WORKERS=3
# user/group to run as
USER=ec2-user
GROUP=ec2-user
cd /srv/www/coral-cobra/project/
source ../env/bin/activate
exec gunicorn project.wsgi:application -w $NUM_WORKERS \
--user=$USER --group=$GROUP
