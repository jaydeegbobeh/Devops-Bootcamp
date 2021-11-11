# Reverse proxy

A reverse proxy is a server that sits in front of web servers and forwards client (e.g. web browser) requests to those web servers.

## Vagrant app requirements

- Nginx folder/files structure
- We want nginx to listen to port 3000 and send traffic to default port 80
- 192.168:10:100 instead nginx default page we should see node-app home-page
- Nginx default config file is located:
    - /etc/nginx/sites-available/default
    - `sudo nano /etc/nginx/sites-available/default` - to update
    - OR
    - `sudo rm -rf /etc/nginx/sites-available/default` - remove this file
    - `sudu nano /etc/nginx/sites-available/default` - write new file with the configuration that we need
    - Add to default file:
        - location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
    - `sudo systenctl restart nginx`
    - `sudo systemctl enable nginx`
     