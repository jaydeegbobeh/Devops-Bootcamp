#!/bin/bash
# update systen
sudo apt-get update -y

# upgrade the packages
sudo apt-get upgrade -y

# install NGINX
sudo apt-get install nginx -y

# load nginx on 192.168.10.100

# nodejs

sudo apt-get install python-software-properties

curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

sudo apt-get install nodejs -y

sudo npm install pm2 -g

node /home/ubuntu/app/Automate_Vagrant_App/starter-code/app/seeds/seed.js

cd /home/ubuntu/app/Automate_Vagrant_App/starter-code/app/
(npm run start&)