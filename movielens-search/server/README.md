# py_api

# api project for presentation

docker access token: py_apy

login:
docker login -u jrod201d

docker-compose run --rm srv sh -c "python manage.py collectstatic"

# view elasticsearch networks:

docker network ls

# Hook up elasticsearch srv

docker run -d \
--name es-container \
--net movielens \
-p 9200:9200 \
-e xpack.security.enabled=false \
-e discovery.type=single-node \
docker.elastic.co/elasticsearch/elasticsearch:7.17.6

=======================

# Kibana srv:

docker run -d \
--name kb-container \
--net movielens \
-p 5601:5601 \
-e ELASTICSEARCH_HOSTS=http://es-container:9200 \
docker.elastic.co/kibana/kibana:7.17.6

Kibana url: http://localhost:5601

======================

# stopping services:

docker container stop kb-container
docker container stop es-container

# view inactive services:

docker ps -a

# start services

docker-compose up -d

=======================

# view active container list

docker container ls  
docker rm -f movielens-srv

# update requirements

pip install -r requirements.dev.txt

=====================

# run migrate & server

chmod +x start.sh
./start.sh

==================

# make migration:

docker-compose exec srv python manage.py makemigrations moviesdoamin
apply changes:
docker-compose exec srv python manage.py migrate
==============

# createsuperuser

docker-compose exec srv python manage.py createsuperuser

docker-compose exec server bash