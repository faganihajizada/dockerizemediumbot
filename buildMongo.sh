#!/bin/sh
docker-compose down
docker-compose up -d
sleep 1
docker exec db_mongodb  mongo admin ./setup/create-admin.js
docker exec db_mongodb mongo telegram ./setup/create-user.js -u superadmin -p super123 --authenticationDatabase admin
