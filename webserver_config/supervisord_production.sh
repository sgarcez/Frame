[program:frame]
directory = /srv/www/coral-cobra/project
user = ec2-user
command = /srv/www/coral-cobra/webserver_config/gunicorn_production.sh
