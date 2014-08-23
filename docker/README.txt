sudo docker pull mpmenne/eve-base

sudo docker run -d mpmenne/eve-base

sudo docker ps -l ...  shows all existing containers

sudo docker inspect {container_name}

ssh root@{container_ip}

# setup the mongodb user ... see README in backend

# clone down the repository for the backend
# git clone https://github.com/MoMenne/global-hack-II

# run the wsgi_app.py in the gh2backend directory
# python wsgi_app.py
