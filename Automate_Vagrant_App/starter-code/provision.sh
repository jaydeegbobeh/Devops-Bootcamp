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

# bashrc

sudo echo 'export DB_HOST="mongodb://192.168.10.150:27017/posts"' >> .bashrc 
source ~/.bashrc

# reverse proxy

sudo rm -rf /etc/nginx/sites-available/default
sudo ln -s /home/vagrant/app/default /etc/nginx/sites-available/
sudo systemctl restart nginx
sudo systemctl enable nginx


# node

node app/app/seeds/seed.js

# start npm
cd /home/vagrant/app/app
sudo npm install
sudo npm install express
node seeds/seed.js





