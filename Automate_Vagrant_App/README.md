# Automate Multiapp Vagrant VM


- create a file for nginx default on localhost
```
upstream nodejs {
  server 192.168.10.100:3000;
  }

  server {
    listen 80;
    location / {
      proxy_pass http://localhost:3000;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Host $host;
      proxy_cache_bypass $http_upgrade;
    }
  }
  ```
- create a file for mongod.conf, update network interfaces sections
```
# network interfaces
net:
  port: 27017
  bindIp: 0.0.0.0
```
- provision.sh for app
```
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
```
- provision.sh for db
```
# be careful of these keys, they will go out of date
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927
echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get update -y
sudo apt-get upgrade -y

# sudo apt-get install mongodb-org=3.2.20 -y
sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20
sudo systemctl restart mongod
sudo system ctl enable mongod

# mongod.conf
sudo rm -rf /etc/mongod.conf
sudo ln -s /home/vagrant/app/mongod.conf /etc/

# if mongo is is set up correctly these will be successful
sudo systemctl restart mongod
sudo systemctl enable mongod

```
- set up an env var once the db is up - in provison.sh file
```
sudo echo 'export DB_HOST="mongodb://192.168.10.150:27017/posts"' >> .bashrc
```

- add dependencies in .gitignore
- restart app and db once conf is changed
